# Identify Analytical Jobs in NHS Wales

Challenge 5 from the May 2023 Wales Modelling Collaborative (WMC) [Data Hackathon for Health Care](https://www.eventbrite.co.uk/e/wmc-data-hackathon-11th-18th-may-2023-tickets-483839706587)

Building on work previously done in https://github.com/stochastictalk/nhs_jobs_data to grab jobs advertised in NHSJobs.

## Day one

Day one was spent looking at the previous work and trying to hone and reimplement it.

* Work trying to extract more information from the website than had been captured previously
* Work removing artefacts that would impact on text analysis (cleaned text data in the data/CleanedDescription files)
* Work looking at the new NHS Jobs website to understand if the original code could be repurposed for the new website framework. The site changes to the new website on 19/05/2023 and currently uses a new click through screen that wasn't there when scraping using the old system.

## Day two

Day two was spent continuing work from day one and starting to do some analysis on the cleaned text dataset

* Continued work trying to extract more information from the website than had been captured previously
* Continued work formatting extracted information to generate a better extract of job information
* Work looking at job evaluations and the way these are used to describe job descriptions and skills to understand if there is a decision tree we can follow to pull out analytical roles - this does not seem to be detailed enough
* Work to try and scrape similar roles from different sites (i.e. civil service) that already include analytical job categorisation. Ideally this will mean we can build a trained classification model to use with our (completely uncategorised) dataset.
* Work trying to visualise some of the information we currently have such as where jobs are being advertised.
* Work trying to identify other sources of information such as the NHS Business Services Authority (NHSBSA) that hosts NHS Jobs and through Freedom of Information (FOI) requests. 
