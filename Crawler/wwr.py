from bs4 import BeautifulSoup 
import requests 
import pandas as pd 

WEBSITE_URL = "https://weworkremotely.com" 
FRONTEND_URL_JOBS = "https://weworkremotely.com/categories/remote-front-end-programming-jobs" 
FRONTEND_URL_JOBS_1 = "https://weworkremotely.com/categories/remote-back-end-programming-jobs" 
FRONTEND_URL_JOBS_2 = "https://weworkremotely.com/categories/remote-full-stack-programming-jobs" 
response = requests.get(FRONTEND_URL_JOBS) 
response_2 = requests.get(FRONTEND_URL_JOBS_1)
response_3 = requests.get(FRONTEND_URL_JOBS_2)
soup = BeautifulSoup(response.text, "html.parser") 

def extract_link(item): 
	item_link = item.find('a') 
	return WEBSITE_URL + item_link.get("href")
	

features = soup.find_all(class_='feature') 
results = [extract_link(item) for item in features]


data = []
for j in results[:50]: 
    another_response = requests.get(j)
    soup1 = BeautifulSoup(another_response.text, "html.parser")
    
    company_title_container = soup1.find(class_='listing-header-container')
    company_name = company_title_container.find('h1').text
    
    company_card = soup1.find(class_='company-card')
    company_logo = company_card.find(class_='listing-logo')
    company_logo = company_logo.find('img')['src']
    company_location = company_card.find('span').text
    company_website = company_card.find('a').get("href")
 
    
    data.append({ 
		"Company Name": company_name, 
        "Logo": company_logo,
        "Location":company_location,
        "Website:":company_website
	}) 

company_data = pd.DataFrame(data) 
company_data.to_json("FrontEnd_Companies.json")

