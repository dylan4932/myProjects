import random
import time
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

from multiprocessing import Pool, freeze_support
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

def variable_init():
    global url
    global driver_path
    global options
    global dataframe
    global Links_list
    global descriptions
    options = Options()
    # headless option
    options.headless = True
    options.binary_location = 'C:\\Program Files\\Mozilla Firefox\\firefox.exe'
    driver_path = "C:/Users/shiva/Desktop/UofT/Term3-Fall2022/APS1624/Assignment 3/geckodriver.exe"

def break_lists(list, n):
    k, m = divmod(len(list), n)
    return (list[i * k + min(i, m):(i + 1) * k + min(i + 1, m)] for i in range(n))

def join_lists(lists):
    return [item for sublist in lists for item in sublist]

def get_url(position, location):
    url_template = "https://www.indeed.com/jobs?q={}&l={}"
    return url_template.format(position, location)


def scrape_posts(postings_list):
    url = get_url("data scientist", "remote")
    options = Options()
    options.headless = True
    options.binary_location = 'C:\\Program Files\\Mozilla Firefox\\firefox.exe'
    driver_path = "C:/Users/shiva/Desktop/UofT/Term3-Fall2022/APS1624/Assignment 3/geckodriver.exe"
    dataframe = pd.DataFrame(columns=["Title", "Company", "Location", "Rating", "Date", "Salary", "Description", "Links"])
    driver = webdriver.Firefox(executable_path=driver_path, options=options)
    
    for i in postings_list:
        driver.get(url + "&start=" + str(i))
        driver.implicitly_wait(3)

        jobs = driver.find_elements(By.CLASS_NAME, 'job_seen_beacon')

        for job in jobs:
            result_html = job.get_attribute('innerHTML')
            soup = BeautifulSoup(result_html, 'html.parser')
            
            
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

            dataframe = pd.concat([dataframe, pd.DataFrame([[title, company, location, rating, date, salary, description, links]], columns=["Title", "Company", "Location", "Rating", "Date", "Salary", "Description", "Links"])], ignore_index=True)
    driver.quit()
    return dataframe


def scrape_postings(postings, n_pros):
    ## Number of postings to scrape
    postings_list = break_lists(list(range(0, postings, 10)), n_pros)
    data = []
    p = Pool(n_pros)
    data = p.map(scrape_posts, postings_list)
    p.close()
    p.join()
    return pd.concat(data, ignore_index=True)


def get_job_description(links):
    options = Options()
    options.headless = True
    options.binary_location = 'C:\\Program Files\\Mozilla Firefox\\firefox.exe'
    driver_path = "C:/Users/shiva/Desktop/UofT/Term3-Fall2022/APS1624/Assignment 3/geckodriver.exe"
    driver = webdriver.Firefox(executable_path=driver_path, options=options)
    descriptions = []
    for link in links:
        driver.get(link)
        driver.implicitly_wait(random.randint(3, 8))
        descriptions.append(driver.find_element(By.XPATH, '//div[@id="jobDescriptionText"]').text)
        time.sleep(random.randint(5,10))
    driver.quit()
    return descriptions


def main():
    random.seed(0)
    print("start")
    variable_init()
    n_pros = 12
    postings = 100
    position = "data scientist"
    locations = "remote"
    url = get_url(position, locations)
    dataframe = scrape_postings(postings, n_pros)
    Links_list = dataframe['Links'].tolist()
    p = Pool(n_pros)
    descriptions = p.map(get_job_description, break_lists(Links_list, n_pros))
    descriptions = join_lists(descriptions)
    p.close()
    p.join()
    dataframe['Descriptions'] = descriptions
    dataframe.to_csv('indeed_jobs_mp.csv', index=False)

if __name__ == '__main__':
    start = time.time() # start time
    freeze_support()
    main()
    end = time.time() # end time
    print("Time taken: ", end - start)
