from bs4 import BeautifulSoup
import requests
import json

class job_scraper:
    """Give the root url with no params. Hardcoded with https://www.jobs.nhs.uk/xi/search_vacancy?"""

    def __init__(self,pages_to_scrape=10):
        self.link = "https://www.jobs.nhs.uk/xi/search_vacancy?"
        self.page_number = 1
        self.pages = pages_to_scrape
        self.max_result = 100
        self.url = self.link + "action=search&page=" + str(self.page_number) + "&max_result=" + str(self.max_result)
        self.search = "?action=search"
        self.page_url = "?action=page&page=" + str(self.page_number)
        self.response = self.__get_response()
        self.link_ok = self.__valid_link()
        self.found_vacancies = self.__get_adverts()
        #self.link_has_search = self.__link_contains_search()

    def __get_response(self):
        return requests.get(self.url)

    def get_next_page(self):
        self.page_number += 1
        self.url = self.__update_url()
        self.found_vacancies = self.__get_adverts()

    def __update_url(self):
        self.url = self.link + "action=search&page=" + str(self.page_number) + "&max_result=" + str(self.max_result)

    def __valid_link(self):
        return self.link.rfind('/')==len(self.link)-1

    def __link_needs_search_param(self):
        return not self.link.endswith('?action=search')
    

    def __get_adverts(self):
        #response = self.__get_response()
        soup = BeautifulSoup(self.response.text,'html.parser')
        return soup.find_all('div',class_="vacancy")
    
    def print_content(self):
        print(self.response.text)

class advert_parser:
    def __init__(self,advert):
        self.vacancy_advert = advert
        self.job_title = self.__get_job_title()
        self.agency = self.__get_agency()
        self.job_description = self.__get_description()
        self.job_subtitle = self.__get_subtitle()
        self.salary = self.__get_advert_bottom("left")[0]
        self.posted_date = self.__get_advert_bottom("left")[1]
        self.job_type = self.__get_advert_bottom("left")[2]
        self.closing_date = self.__get_advert_bottom("right")[0]
        self.staff_group = self.__get_advert_bottom("right")[1]
        self.job_ref = self.__get_advert_bottom("right")[2]
        self.dict = {"title":self.job_title,"subtitle":self.job_subtitle,"agency":self.agency,
        "job_description":self.job_description,"salary":self.salary,"posted_date":self.posted_date,"job_type":self.job_type,
        "closing_date":self.closing_date,"staff_group":self.staff_group,"job_ref":self.job_ref}

    def __get_job_title(self):
        for link in self.vacancy_advert.find('h2').find_all('a'):
            return link['title']
    
    def __get_subtitle(self):
        return self.vacancy_advert.find('h3').text

    def __get_agency(self):
        return self.vacancy_advert.find('p',class_="agency").strong.text

    def __get_description(self):
        return self.vacancy_advert.find_all('p')[1].text

    def __get_advert_bottom(self,side:str):
        section = self.vacancy_advert.find('div',class_=side).find_all('dd')
        return (section[0].text.replace('\n','').strip(),section[1].text.replace('\n','').strip(),section[2].text.replace('\n','').strip())

    def create_json(self):
        return json.dumps(self.dict,ensure_ascii=False)

    