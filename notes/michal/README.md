# Michał's Notes

We can only look at the information publically available at https://www.jobs.nhs.uk/. 
This limits the amount of data we have to work with, at least right now. 

[National Archives](https://nationalarchivies.org.uk) contains historical versions of the https://www.jobs.nhs.uk/ website.
This could provide us with more data, but the only API available, the [Discovery](https://discovery.nationalarchives.gov.uk/) allows only to brows the content catalogue. 
The API appears not to be open, it requires registration and submitting an IP address. 
**It is not feasible to use it in the time constraints we have**


## ML Categorisation Approach
This is an alternative approach to the initial one based on Natural Language Processing (NLP).

The job descriptions, we expect, are not standard and lack standard labels. 
This is because NHS does not implement [Digital Data and Technology Profession Capability Framework (DDaT)](https://www.gov.uk/government/collections/digital-data-and-technology-profession-capability-framework) or similar. 
The initial thoughts were of using NLP to extract useful information - perhaps a more suitable approach when the dataset is limited. 

However, we can take advantage of the fact that other parts of government implement DDaT framework. 
We can scrape [Civil Service Jobs](civilservicejobs.service.gov.uk) service looking for interesting job descriptions:
data analyst, data scientists, and so on. 
We could try to apply similar technique on [NHS Jobs](https://www.jobs.nhs.uk/) and supplement this with datasets from [Kaggle](https://www.kaggle.com/datasets?search=job+description). 
I have checked, there are a few relevant free datasets available. 
They are not exactly what we need, but I think they might be close enough to give use reasonable level of success. 

This should give us enough data to train an Machine Learning (ML) model to take a job description, and predict a label - the job description. 
With a model developed we could run it on all NHS Jobs listings and identify jobs of interest. 
