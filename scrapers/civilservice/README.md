# CivilServiceJobs.services.gov.uk scraper

The script searches for specific job categories and traverses all the results
capturing the details in JSON format in individuals files in `./data/` folder. 

This data could be collected and used to train categorisation models to predict 
a label - the job title or category - based on the job description. 

An example:

```json
{
  "role": "DIO -  People Team Data Analyst",
  "reference": "286947",
  "employer": "Ministry of Defence",
  "locations": [
    "Lichfield:DMS Whittington",
    " WS14 9PY",
    " Catterick:Piave Lines",
    " DL9 3LR",
    " Tidworth:Canada House",
    " SP9 7BS"
  ],
  "salary": {
    "min": 33830,
    "max": 33830
  },
  "closing_date": "2023-05-19T23:55:00",
  "details": {
    "Reference number": "286947",
    "Salary": "33,830",
    "Job grade": "Higher Executive Officer",
    "Contract type": "Permanent",
    "Business area": "MOD - Defence Infrastructure Organisation - People Team",
    "Type of role": "Analytical",
    "Working pattern": "Flexible working, Full-time, Job share, Part-time, Compressed Hours",
    "Number of jobs available": "1",
    "Job summary": "Do you want to work for the Defence Infrastructure Organisation (DIO) and play a key role in keeping our country safe through caring for the Defence estate and those that depend on it? DIO manages the Defence estate, one of the UK's largest and most diverse property portfolios, enabling the armed forces and Defence civilians to live, work, train and deploy. From net carbon-zero accommodation to runways for the F35 fighter jets, our outputs are unique in the UK and across the globe!Learn much more about DIO in our Candidate Information Guide attached.About DIOView our YouTube video to see more about our work",
    "Job description": "The People Team provide specialist HR expertise to DIO. We work alongside Defence Business Services (DBS) and MOD Civilian HR to develop a flexible and dynamic workforce that is suitably qualified, innovative, and highly productive. We work closely with business areas to understand their specific needs and challenges, and tailor our approach and services to achieve the best outcomes.The scope of our services range from promoting Diversity and Inclusion and employee engagement, through to working with Trade Unions and advising the DIO Executive Committee (ExCo) on both tactical and strategic HR matters.The Data Analyst role is responsible for delivering a wide variety of people management information (MI) across the business to a variety of customers including senior Leaders and Business Management Teams, aiding and supporting them to make clear decisions and deliver against people related objectives. The role requires an eye for detail ensuring the data is accurate, meets data protection regulations and is accurately maintained.The role is pivotal in supporting the team's day to day activity, and has ownership of producing the People Data Packs and Data Report (PDR) from Cognos and MyHR systems. The incumbent will also produce insightful deep dives and analysis on numerous subjects producing reports and dashboards that will be presented to different senior leadership boards including the Executive Committee.The successful candidate will work with, and provide support to teams both internally within DIO and externally in the wider MOD, to ensure DIO People Data reporting is at the forefront of technological capabilities and ensure we continue to build on our positive reputation.",
    "Person specification": "The key responsibilities for the role are as follows...Responsible for the continuous improvement and delivery of the DIO People Data Packs and the People Data Reports (PDR) to each area of the business on a monthly business.Responsible for a number of (but not limited to) People Team Data Team scheduled report production such as; Executive Committee return, Mandatory Training Report, Cabinet Office Organogram return.Be the DIO focal point to DBS, and being the gateway for all scheduled reporting and ad hoc data requests from the business for people data.Manipulate Excel data to produce accurate reporting tables for Senior Leaders including pivoting, writing macros and formula use. And where possible, look to streamline the reporting using automation to save both time and resource.Working together with the HR Business Partners to ensure DIO business areas are being provided with the right people MI. Attend DIO Business Area Working Groups and HR Business Partner (HRBP)Coordinate monthly audits of MyHR People reports to ensure accuracy.Support to the Data Lead in their role of Data Steward, Data Protection Focal Point and Security Administrator.Other tasks, as the need arises, in support of the wider DIO People Team function.Desirable Skills & Experience A background in Data Analytics.\ An enhanced, competent user of Microsoft Excel and experienced user of other Microsoft Office Suite of tools (Word, Power Point). Strong communication and interpersonal skills.",
    "Behaviours": "We'll assess you against these behaviours during the selection process: Delivering at Pace\nManaging a Quality Service\nChanging and Improving\nMaking Effective Decisions\nWorking Together\nWe only ask for evidence of these behaviours on your application form:Delivering at Pace\nManaging a Quality Service\n",
    "Selection process details": "This vacancy is using Success Profiles (opens in a new window), and will assess your Behaviours and Experience.",
    "Security": "Successful candidates must meet the security requirements before they can be appointed. The level of security needed is security check (opens in a new window).See our vetting charter (opens in a new window).",
    "Nationality requirements": "This job is broadly open to the following groups:\n\nUK nationals\nnationals of Commonwealth countries who have the right to work in the UK\nnationals of the Republic of Ireland\nnationals from the EU, EEA or Switzerland with settled or pre-settled status or who apply for either status by the deadline of the European Union Settlement Scheme (EUSS) (opens in a new window)\nrelevant EU, EEA, Swiss or Turkish nationals working in the Civil Service\nrelevant EU, EEA, Swiss or Turkish nationals who have built up the right to work in the Civil Service\ncertain family members of the relevant EU, EEA, Swiss or Turkish nationals\n\nFurther information on nationality requirements (opens in a new window)\n",
    "Working for the Civil Service": "The Civil Service Code (opens in a new window) sets out the standards of behaviour expected of civil servants.We recruit by merit on the basis of fair and open competition, as outlined in the Civil Service Commission's recruitment principles (opens in a new window).",
    "Contact point for applicants": "Job contact : Name : Clair SimonEmail : clair.simon875@mod.gov.ukRecruitment teamEmail : DBSCivPers-DIOResourcing@mod.gov.uk",
    "Further information": "Applicants should monitor their Civil Service Jobs application centre regularly for updates.Some of MoD's Terms and Conditions of Service (TACOS) changed from 3 February 2014. Those TACOS changes applied to Broader Banded and Skill Zone staff who were new recruits to MoD or who were appointed to a post on substantive promotion, progression or advancement. On the same basis, the TACOS for Departmental Retained Grades changed with effect from 01 September 2014. The document attached to this advertisement provides more information.All employees joining MOD who are new to the Civil Service will be subject to a 6-month probation period (unless otherwise advised) effective from the employment start date.  Any move to Ministry of Defence from another employer will mean you can no longer access childcare vouchers. This includes moves between government departments. You may however be eligible for other government schemes, including Tax-Free Childcare. Determine your eligibility at www.childcarechoices.gov.ukIf you need to contact Defence Business Services (DBS) regarding this vacancy, please contact the DIO Enhanced Recruitment Team on  DBSCivPers-DIOResourcing@mod.gov.ukComplaintsPlease be aware that the selection and interviewing of applicants is the responsibility of the Recruiting Line Manager (RLM) and not the Defence Business Services (DBS) Resourcing team. DBS do not play any part in the selection and interview process.Therefore, if you wish to discuss your feedback, or you are dissatisfied with your markings, you should in the first instance raise this with the Recruiting Line Manager of the vacancy.If you are dissatisfied with the service you have received from DBS, or believe that DBS has failed to follow the recruitment process in line with the Civil Service Commission principles of selection for appointment on merit on the basis of Fair and Open competition, you can raise a formal complaint by writing to DBS at the following address:Defence Business Services, Scanning Hub, PO Box 38, Cheadle Hulme, SK8 7NUIf after raising your complaint with DBS you remain dissatisfied you can complain directly to the Civil Service Commission at the following address: Civil Service commission, Room G/8, 1 Horse Guards Road, London, SW1A 2HQOr by email:  info@csc.gov.ukCabinet Office Fraud ChecksApplicants who are successful at interview will be, as part of pre-employment screening, subject to a check on the Internal Fraud Database (IFD). This check will provide information about employees who have been dismissed for fraud or dishonesty offences. This check also applies to employees who resign or otherwise leave before being dismissed for fraud or dishonesty had their employment continued. Any applicant whose details are found to be held on the IFD will be refused employmentCivil Service Recruitment PrinciplesPlease see the link below for the civil service recruitment principles. https://civilservicecommission.independent.gov.uk/recruitment/recruitment-principles/To find out a bit more about what it's like working for MOD, visit the Civil Service Careers Website https://www.civil-service-careers.gov.uk/departments/working-for-the-ministry-of-defence/ Please see the MOD Privacy Notice link below which describes how we will use your personal data, explains your rights and gives you information you are entitled to under Data Protection legislation.https://www.gov.uk/government/publications/ministry-of-defence-privacy-notice/mod-privacy-noticeTravel Costs There will be no reimbursement for any travel expenses for the interview.Nationality StatementAs a result of the changes to the UK immigration rules which came into effect on 1 January 2021, the Ministry of Defence will only offer sponsorship for a skilled worker visa under the points-based system, where a role has been deemed to be business critical. The role currently being advertised has not been assessed as business critical and is therefore NOT open to applications from those who will require sponsorship under the points-based system. Should you apply for this role and be found to require sponsorship, your application will be rejected, and any provisional offer of employment withdrawn.Smoke-Free Working Environment PolicyThe Ministry of Defence is committed to providing a safe and healthy working environment for its staff which includes educating them on the benefits of not smoking, protecting them from the harmful effects of second-hand smoke and supporting those who want to give up smoking. Under the Smoke-Free Working Environment policy, Smoking and the use of all tobacco products (including combustible and chewing tobacco products) will not be permitted anywhere in the Defence working environment by 31st December 2022. The policy is Whole Force and includes all Defence personnel, contractors, visitors and other non-MOD personnel. All applicants seeking, considering, or accepting employment with the Ministry of Defence should be aware of this policy and that it is already in place at a number of Defence Establishments."
  },
  "hash": "0de8324e6589ec4676ee511751481cef"
}
```

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
