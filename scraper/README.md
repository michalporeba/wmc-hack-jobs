# Scraper

The class job_scraper searches the NHS jobs site and advert_parser gets information about a vacancy. To export a list of vacancies use the scraper to scrape a page, the advert_parser to parse an advert and then use the create_json method to save the parsed file.

```
scraper = job_scraper(pages_to_scrape=1)
for page in range(scraper.pages):
    for advert in scraper.found_vacancies:
        parsed_advert = advert_parser(advert)
        with open(parsed_advert.job_ref + ".json","w",encoding='utf-8') as file:
            file.write(parsed_advert.create_json())
    scraper.get_next_page()
```