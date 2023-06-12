import random
import time
import pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

start = time.time()
random.seed(0)

options = Options()
options.binary_location = 'C:\\Program Files\\Mozilla Firefox\\firefox.exe'

# Ensure that the driver path is correct before running this script.
# Microsoft Windows
driver_path = "C:/Users/shiva/Desktop/UofT/Term3-Fall2022/APS1624/Assignment 3/geckodriver.exe"
# Linux
#driver_path = "./drivers/linux/geckodriver"
driver = webdriver.Firefox(executable_path=driver_path, options=options)

## Enter a job position
position = "data scientist"
## Enter a location (City, State or Zip or remote)
locations = "remote"

def get_url(position, location):
    url_template = "https://www.indeed.com/jobs?q={}&l={}"
    url = url_template.format(position, location)
    return url

url = get_url(position, locations)
dataframe = pd.DataFrame(columns=["Title", "Company", "Location", "Rating", "Date", "Salary", "Description", "Links"])

## Number of postings to scrape
postings = 100

jn=0
for i in range(0, postings, 10):

    driver.get(url + "&start=" + str(i))
    driver.implicitly_wait(3)

    jobs = driver.find_elements(By.CLASS_NAME, 'job_seen_beacon')

    for job in jobs:
        result_html = job.get_attribute('innerHTML')
        soup = BeautifulSoup(result_html, 'html.parser')
        
        jn += 1
        
        liens = job.find_elements(By.TAG_NAME, "a")
        links = liens[0].get_attribute("href")
        
        title = soup.select('.jobTitle')[0].get_text().strip()
        company = soup.select('.companyName')[0].get_text().strip()
        location = soup.select('.companyLocation')[0].get_text().strip()
        try:
            salary = soup.select('.salary-snippet-container')[0].get_text().strip()
        except:
            salary = 'NaN'
        try:
            rating = soup.select('.ratingNumber')[0].get_text().strip()
        except:
            rating = 'NaN'
        try:
            date = soup.select('.date')[0].get_text().strip()
        except:
            date = 'NaN'
        try:
            description = soup.select('.job-snippet')[0].get_text().strip()
        except:
            description = ''
       
        dataframe = pd.concat([dataframe, pd.DataFrame([{'Title': title,
                                          "Company": company,
                                          'Location': location,
                                          'Rating': rating,
                                          'Date': date,
                                          "Salary": salary,
                                          "Description": description,
                                          "Links": links}])], ignore_index=True)
        #print("Job number {0:4d} added - {1:s}".format(jn,title))

driver.quit()

Links_list = dataframe['Links'].tolist()

descriptions=[]
driver = webdriver.Firefox(executable_path=driver_path, options=options)
for i in Links_list:
    driver.get(i)
    driver.implicitly_wait(random.randint(3, 8))
    jd = driver.find_element(By.XPATH, '//div[@id="jobDescriptionText"]').text
    descriptions.append(jd)
    time.sleep(random.randint(5,10))

dataframe['Descriptions'] = descriptions
driver.quit()

# Convert the dataframe to a csv file
date = datetime.today().strftime('%Y-%m-%d')
dataframe.to_csv(date + "_" + position + "_" + locations + ".csv", index=False)

end = time.time()
print("Time taken to scrape: {0:.2f} seconds".format(end - start))

