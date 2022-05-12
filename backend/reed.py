from bs4 import BeautifulSoup 
import requests 
import pandas as pd 


WEBSITE_URL = "https://www.reed.co.uk" 
FRONTEND_URL_JOBS = "https://www.reed.co.uk/jobs/work-from-home-jobs" 
response = requests.get(FRONTEND_URL_JOBS) 

s = BeautifulSoup(response.text, "html.parser")

def extract_link(item):
    item_link = item.find('a')
    return WEBSITE_URL + item_link.get('href')


job_result_heading = s.find_all(class_='job-result-heading__posted-by')
results = [extract_link(item) for item in job_result_heading]

data = []
for item in results[:20]:
    another_response = requests.get(item)
    soup1 = BeautifulSoup(another_response.text, "html.parser")
    
    links =[]
    wrapp = soup1.find(class_='recruiter-description')
    try:
        c_link = wrapp.find('a').get('href')
        links.append({
            "link": c_link
        })
    except:
        c_link = ''
    
   
    for link in links:
        another_response_1 = requests.get(WEBSITE_URL + link['link'])
        soup2 = BeautifulSoup(another_response_1.text, "html.parser")
        
        company_name_wrapper = soup2.find(class_='heading')
        company_name = company_name_wrapper.find(class_='title').text
        
        company_info_list = soup2.find(class_="information__list")
        company_li = company_info_list.find_all('li')
        d = []
        for li in company_li:
            p = li.find_all('span', attrs={'class': 'information__description'})
            d.append(p)
            
        g = []
        for x in d:
            g.append(x[0])
        try:
            company_size = g[0].text
        except:
            company_size = ''
        try:
            company_sector = g[1].text
        except:
            company_sector = ''
        try:
            company_location = g[2].text  
        except:
            company_location = ''
        
           
        
        data.append({ 
            "Company Name": company_name, 
            "Size": company_size,
            "Sector:":company_sector
        }) 
    
    
company_data = pd.DataFrame(data) 
company_data.to_json("Reed_Companies.json")
      