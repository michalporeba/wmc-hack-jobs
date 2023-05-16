import re
import requests
from bs4 import BeautifulSoup
import logging as log

log.basicConfig(level=log.DEBUG)

BASE_URL = 'https://www.civilservicejobs.service.gov.uk'

session = requests.Session()

# Send HTTP request to URL
response = session.get(BASE_URL)

# Parse HTML response
page = BeautifulSoup(response.text, 'html.parser')

form = page.select_one('form', id='update_cookie_preferences_form')
if (form != None):
    log.info('Cookie form shown - attempting to reject non-essential cookies')
    action_url = form.get('action')
    if action_url == None:
        log.error('Unable to find action for the cookie form')
    action_url = BASE_URL + action_url
    log.debug(f'action_url = {action_url}')
    
    update_token = form.select_one('input', name='cookie_update_token')['value']
    if update_token == None:
        log.error('Unable to find hidden input `cookie_update_token`.')
    log.debug(f'update_token = {update_token}')

    response = session.post(action_url, { 'cookie_update_token': update_token, 'accept_essential_cookies_button': 'Reject additional cookies'})
    if not response.ok: 
        log.error('Server returned an error!')
        log.error(response.reason)
else: 
    log.warn('Expected a cookie acceptance form, but it was not found. Chec, if the Id is still `update_cookie_preferences_form`.')

    
page = BeautifulSoup(response.text, 'html.parser')
log.debug("Looking for the search form")
forms = page.find_all('form', method='post')
search_form = None 

for form in forms:
    if 'esearch.cgi' in form['action']:
        search_form = form
        break 
    
if search_form == None:
    log.error('The search form was not found on the page. Check if the expected action is still to `esearch.cgi`.')

action_url = search_form['action']
form_data = {}
for input in search_form.find_all('input'):
    form_data |= {input.get('name'): input.get('value')}

form_data['what'] = 'data'

response = session.post(action_url, form_data)
if not response.ok: 
    log.error('Server returned an error!')
    log.error(response.reason)

page = BeautifulSoup(response.text, 'html.parser')

next = page.select_one('a[title="Go to next search results page"]')
print(next)
jobs = page.select_one('ul', title='Job list')
#print(jobs)

