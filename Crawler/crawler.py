import requests 
from bs4 import BeautifulSoup 
 
WEBSITE_URL = "https://weworkremotely.com" 
FRONTEND_URL_JOBS = "https://weworkremotely.com/categories/remote-front-end-programming-jobs" 
response = requests.get(FRONTEND_URL_JOBS) 
soup = BeautifulSoup(response.text, "html.parser") 

def extract_link(item): 
	item_link = item.find('a') 
	return { 
         "link": WEBSITE_URL + item_link.get("href")
    }
try: 
	if response.ok: 
		features = soup.find_all(class_='feature') 
        # results = [extract_link(item) for item in features]
        print(features)
        # details = []
        # for j in results:
        #     response1 = requests.get(WEBSITE_URL + j["link"])
        #     soup1 = BeautifulSoup(response1.text, "html.parser") 

        #     container = soup1.find(class_='listing-header-container')
        #     print(container)    
	else: 
		print(response) # status_code is 4XX or 5XX 
except Exception as e: 
	print(e)