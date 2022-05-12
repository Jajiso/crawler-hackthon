from bs4 import BeautifulSoup 
import requests 
import pandas as pd 

headers = {'User-Agent': 'Mozilla/5.0'}
WEBSITE_URL = "https://devitjobs.uk/" 
FRONTEND_URL_JOBS = "https://devitjobs.uk/jobs/JavaScript/London" 
response = requests.get(FRONTEND_URL_JOBS, headers=headers) 

s = BeautifulSoup(response.text, "html.parser")

def extract_link(item):
    item_link = item.find('a')
    return WEBSITE_URL + item_link.get('href')

wrapper = s.find(class_='job-postings-wrapper')
job_results = s.find('article')
# results = [extract_link(item) for item in job_result]

print(s)