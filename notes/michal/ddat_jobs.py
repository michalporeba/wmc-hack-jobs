import re
import requests
from bs4 import BeautifulSoup
import logging as log

log.basicConfig(level=log.DEBUG)

# Define URL
# https://www.civilservicejobs.service.gov.uk/csr/index.cgi?SID=cGFnZWFjdGlvbj1zZWFyY2hjb250ZXh0JmNvbnRleHRpZD0zNTczOTI2MSZvd25lcnR5cGU9ZmFpciZvd25lcj01MDcwMDAwJnBhZ2VjbGFzcz1TZWFyY2gmcmVxc2lnPTE2ODQxOTIwMDktNWUwMTVhMGU3MDgxZDNjYjk4MmI5NmYwZjQ3NjIzOTk4ODU0ZDUyZg==
# https://www.civilservicejobs.service.gov.uk/csr/index.cgi?SID=b3duZXJ0eXBlPWZhaXImY29udGV4dGlkPTM1NzM5NDI5JnBhZ2VhY3Rpb249c2VhcmNoY29udGV4dCZvd25lcj01MDcwMDAwJnBhZ2VjbGFzcz1TZWFyY2gmcmVxc2lnPTE2ODQxOTIzNDEtMjgxYTM2OTI3YWJmMmM4OTY1ODZlYmRlN2MxMDc2MDQ5ODBhMTU2MQ==


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
print("Looking for forms")
forms = page.find_all('form', method='post')
for form in forms:
    print(form['action'])

print("DONE")
# Find all job postings
#agencies = soup.find_all('div', {'class': 'agencyAdvert'})

# Extract information from each job posting
#for agency in agencies:
#    agency_link = agency.select_one('h3 > a', href=True)
#    name = agency_link.text 
#    url = agency_link['href']
#    agency_id = re.search(r".*agency_id=(?P<agency_id>\d+)", url)['agency_id']

#    print(name)
#    print(agency_id)
#    print('-------')

    #title = job.find('a', {'class': 'jobTitle'}).text
    #description = job.find('p', {'class': 'jobDesc'}).text
    #location = job.find('span', {'class': 'jobLocation'}).text
    #print(f'Title: {title}\nDescription: {description}\nLocation: {location}\n')
