import re
import sys
import requests
from bs4 import BeautifulSoup, element
import logging as log
from datetime import datetime 

log.basicConfig(level=log.INFO)

BASE_URL = 'https://www.civilservicejobs.service.gov.uk'
SALARIES_REGEX = re.compile(r"^.*£(?P<from>\d{1,3},\d{3}).*£?(?P<to>\d{1,3},\d{3})?$")

def reject_nonessential_cookies(session:requests.Session) -> bool:
    response = session.get(BASE_URL)
    page = BeautifulSoup(response.text, 'html.parser')

    form = page.select_one('form', id='update_cookie_preferences_form')
    if (form != None):
        log.info('Cookie form shown - attempting to reject non-essential cookies')
        action_url = form.get('action')
        if action_url == None:
            log.error('Unable to find action for the cookie form')
            sys.exit()
        
        action_url = BASE_URL + action_url
        log.debug(f'action_url = {action_url}')
        
        update_token = form.select_one('input', name='cookie_update_token')['value']
        if update_token == None:
            log.error('Unable to find hidden input `cookie_update_token`.')
            sys.exit()
        log.debug(f'update_token = {update_token}')

        response = session.post(action_url, { 'cookie_update_token': update_token, 'accept_essential_cookies_button': 'Reject additional cookies'})
        if_error_report_reason_and_quit(response)
        
    else: 
        log.warn('Expected a cookie acceptance form, but it was not found. Chec, if the Id is still `update_cookie_preferences_form`.')
    


def get_search_form(session:requests.Session, page:element.Tag) -> element.Tag:
    log.debug('Looking for the search form in the page')
    for form in page.find_all('form', method='post'):
        if 'esearch.cgi' in form['action']:
            return form
    
    return None


def get_search_form_data_for_keyword(session:requests.Session, form, keyword:str):
    form_data = {}
    for input in form.find_all('input'):
        form_data |= {input.get('name'): input.get('value')}

    form_data['what'] = keyword
    return form_data


def if_error_report_reason_and_quit(response:requests.Response):
    if not response.ok: 
        log.error('Server returned an error!')
        log.error(response.reason)
        sys.exit()


def get_datetime_from_description(description:str) -> datetime:
    pattern = r'^(.*\d+)(st|nd|rd|th)(.*)$'
    description = re.sub(pattern, r'\1\3', description)
    description = description.replace('Closes : ', '')
    return datetime.strptime(description, '%I:%M %p on %A %d %B %Y')


def capture_job(session:requests.Session, job_list_item:element.Tag) -> dict:
    job_link = job_list_item.select_one('h3[class="search-results-job-box-title"] > a')
    job_url = job_link['href']
    
    job = { 'title': job_link.text }
    job['reference'] = job_list_item.select_one('div[class="search-results-job-box-refcode"]').text.replace('Reference : ','')
    job['employer'] = job_list_item.select_one('div[class="search-results-job-box-department"]').text.replace('at ', '')
    job['locations'] = job_list_item.select_one('div[class="search-results-job-box-location"]').text.strip().split(',')
    job['salary'] = {}
    salary_description = job_list_item.select_one('div[class="search-results-job-box-salary"]').text
    salary = re.match(SALARIES_REGEX, salary_description)
    if salary and 'from' in salary.groupdict():
        job['salary']['min'] = int(salary.group('from').replace(',',''))
        if salary.group('to') is not None:
            job['salary']['max'] = int(salary.group('to').replace(',','')) 
        else:
            job['salary']['max'] = job['salary']['min']
    
    closing_date = job_list_item.select_one('div[class="search-results-job-box-closingdate"]').text
    job['closing_date'] = get_datetime_from_description(closing_date)

    return job


def get_job_list_by_keyword(session:requests.Session, keyword:str) -> bool:
    log.debug(f'Looking for {keyword} jobs')
    
    response = session.get(BASE_URL)
    if_error_report_reason_and_quit(response)
    
    search_form = get_search_form(session, BeautifulSoup(response.text, 'html.parser'))

    if search_form == None:
        log.error('The search form was not found on the page. Check if the expected action is still to `esearch.cgi`.')
        sys.exit()

    form_data = get_search_form_data_for_keyword(session, search_form, keyword)
    action_url = search_form['action']
    
    response = session.post(action_url, form_data)
    if_error_report_reason_and_quit(response)

    while True:
        page = BeautifulSoup(response.text, 'html.parser')
        next = page.select_one('a[title="Go to next search results page"]')

        jobs = page.select_one('ul[title="Job list"]')
        for job in jobs.select('li[class="search-results-job-box"]'):
            data = capture_job(session, job)
            print(data)
    
        if not next:
            break 

        response = session.get(next['href'])


def get_jobs(session:requests.Session) -> bool:
    job_titles = ['data analyst'] #, 'data engineer']
    for job_title in job_titles:
        if not get_job_list_by_keyword(session, job_title):
            sys.exit()


session = requests.Session()
actions = [reject_nonessential_cookies, get_jobs]

for action in actions:
    action(session)