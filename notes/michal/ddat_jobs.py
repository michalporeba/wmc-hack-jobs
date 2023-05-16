import re
import requests
from bs4 import BeautifulSoup
import logging as log

log.basicConfig(level=log.INFO)

BASE_URL = 'https://www.civilservicejobs.service.gov.uk'

def reject_nonessential_cookies(session:requests.Session) -> bool:
    response = session.get(BASE_URL)
    page = BeautifulSoup(response.text, 'html.parser')

    form = page.select_one('form', id='update_cookie_preferences_form')
    if (form != None):
        log.info('Cookie form shown - attempting to reject non-essential cookies')
        action_url = form.get('action')
        if action_url == None:
            log.error('Unable to find action for the cookie form')
            return False
        
        action_url = BASE_URL + action_url
        log.debug(f'action_url = {action_url}')
        
        update_token = form.select_one('input', name='cookie_update_token')['value']
        if update_token == None:
            log.error('Unable to find hidden input `cookie_update_token`.')
            return False
        log.debug(f'update_token = {update_token}')

        response = session.post(action_url, { 'cookie_update_token': update_token, 'accept_essential_cookies_button': 'Reject additional cookies'})
        if not response.ok: 
            log.error('Server returned an error!')
            log.error(response.reason)
            return False 
    else: 
        log.warn('Expected a cookie acceptance form, but it was not found. Chec, if the Id is still `update_cookie_preferences_form`.')

    return True
    

def get_job_lists(session:requests.Session) -> bool:
    pass


def get_job_list_by_keyword(session:requests.Session, keyword:str) -> bool:
    log.debug(f'Looking for {keyword} jobs')
    
    response = session.get(BASE_URL)
    if not response.ok: 
        log.error('Server returned an error!')
        log.error(response.reason)
        return False 
    
    log.debug('Looking for the search form in the page')
    page = BeautifulSoup(response.text, 'html.parser')

    forms = page.find_all('form', method='post')
    search_form = None 

    for form in forms:
        if 'esearch.cgi' in form['action']:
            search_form = form
            break 
        
    if search_form == None:
        log.error('The search form was not found on the page. Check if the expected action is still to `esearch.cgi`.')
        return False 

    form_data = {}
    for input in search_form.find_all('input'):
        form_data |= {input.get('name'): input.get('value')}

    form_data['what'] = keyword
    action_url = search_form['action']
    
    response = session.post(action_url, form_data)
    if not response.ok: 
        log.error('Server returned an error!')
        log.error(response.reason)
        return False
    
    while True:
        page = BeautifulSoup(response.text, 'html.parser')
        
        jobs = page.select_one('ul[title="Job list"]')
        for job in jobs.select('li[class="search-results-job-box"]'):
            job_link = job.select_one('h3[class="search-results-job-box-title"] > a')
            job_url = job_link['href']
            job_title = job_link.text
            print(f'{job_title} -> {job_url}')
    
        next = page.select_one('a[title="Go to next search results page"]')
        if not next:
            break 

        response = session.get(next['href'])

    return True


def get_jobs(session:requests.Session) -> bool:
    job_titles = ['data analyst', 'data engineer']
    for job_title in job_titles:
        if not get_job_list_by_keyword(session, job_title):
            return False

    return True 


def stop(session:requests.Session) -> bool:
    return False

session = requests.Session()
actions = [reject_nonessential_cookies, get_jobs]

for action in actions:
    if not action(session):
        break 