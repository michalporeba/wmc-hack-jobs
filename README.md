# Identify Analytical Jobs in NHS Wales

Challenge 5 from the May 2023 Wales Modelling Collaborative (WMC) [Data Hackathon for Health Care](https://www.eventbrite.co.uk/e/wmc-data-hackathon-11th-18th-may-2023-tickets-483839706587)

## The objectives

There are many interesting questions that could be answered to better understand
the analytical professions in healthcare if we had data on recruitment. 
Unfortunately, the data is not readily available. What makes it more challenging, 
is that analytical elements are important to many other professions, and the that
the analytical jobs are advertised with varying titles and descriptions and a generic
":"Administrative and Clerical" category. 

Example questions of interest:
* What's the rate at which analytical jobs are advertised  
* Comparison of healthboards and their gaps - job advert  
* How can we recruit and analyse on the jobs.  


### 1. Scraping the NHS job adverts for analytical professions

There is no API, or other bulk access to historic job adverts. First part of the challenge 
is to collect the publically available job adverts for analysis now and in the future. 

### 2. Classification of the job descriptions

Because there is no consistency of how the jobs are advertised
there is a need to find a way to reliably identify jobs where data analysis is not only 
part of requirements, but is core to the profession of data analyst.     

## Notes
### Day one

Day one was spent looking at the previous work and trying to hone and reimplement it.

* Work trying to extract more information from the website than had been captured previously
* Work removing artefacts that would impact on text analysis (cleaned text data in the data/CleanedDescription files)
* Work looking at the new NHS Jobs website to understand if the original code could be repurposed for the new website framework. The site changes to the new website on 19/05/2023 and currently uses a new click through screen that wasn't there when scraping using the old system.

### Day two

Day two was spent continuing work from day one and starting to do some analysis on the cleaned text dataset

* Continued work trying to extract more information from the website than had been captured previously
* Continued work formatting extracted information to generate a better extract of job information
* Work looking at job evaluations and the way these are used to describe job descriptions and skills to understand if there is a decision tree we can follow to pull out analytical roles - this does not seem to be detailed enough
* Work to try and scrape similar roles from different sites (i.e. civil service) that already include analytical job categorisation. Ideally this will mean we can build a trained classification model to use with our (completely uncategorised) dataset.
* Work trying to visualise some of the information we currently have such as where jobs are being advertised.
* Work trying to identify other sources of information such as the NHS Business Services Authority (NHSBSA) that hosts NHS Jobs and through Freedom of Information (FOI) requests. 

## Outcomes

The group produced two scrapers (both have potential for improvements). 

* [NHS jobs scraper](scrapers/nhs/)
* [Civil Service Jobs scraper](scrapers/civilservice/)

We have also explored alternative ways of gather the necessary information

* Through the existing internal processes - the data could be very useful but limited in scope and in its application
* Through Freedom of Information requests - we found examples of similar requests from the past that resulted in data released by NHS

