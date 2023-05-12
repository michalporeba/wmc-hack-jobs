import re
import requests
from bs4 import BeautifulSoup

# Define URL
BASE_URL = 'https://www.jobs.nhs.uk'
WELSH_EMPLOYERS_PATH = '/xi/employer_list/?action=search&sha=S11'
EMPLOYER_JOBS_PATH = '/xi/search_vacancy/?action=search;master_id='

# Send HTTP request to URL
response = requests.get(BASE_URL + WELSH_EMPLOYERS_PATH)

# Parse HTML response
soup = BeautifulSoup(response.text, 'html.parser')

# Find all job postings
agencies = soup.find_all('div', {'class': 'agencyAdvert'})

# Extract information from each job posting
for agency in agencies:
    agency_link = agency.select_one('h3 > a', href=True)
    name = agency_link.text 
    url = agency_link['href']
    agency_id = re.search(r".*agency_id=(?P<agency_id>\d+)", url)['agency_id']

    print(name)
    print(agency_id)
    print('-------')

    #title = job.find('a', {'class': 'jobTitle'}).text
    #description = job.find('p', {'class': 'jobDesc'}).text
    #location = job.find('span', {'class': 'jobLocation'}).text
    #print(f'Title: {title}\nDescription: {description}\nLocation: {location}\n')
