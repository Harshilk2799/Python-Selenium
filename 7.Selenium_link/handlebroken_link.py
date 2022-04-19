from selenium import webdriver 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import requests

service_obj = Service(executable_path="/home/harshil/Selenium/Drivers/chromedriver_linux64/chromedriver")

driver = webdriver.Chrome(service = service_obj)

driver.get("http://www.deadlinkcity.com/")
driver.maximize_window()

links = driver.find_elements(By.TAG_NAME, "a")

count = 0
for link in links:
    url = link.get_attribute("href")
    try:
        res = requests.head(url)
    except:
        None

    if res.status_code >= 400:
        print(url, " Is broken link")
        count += 1
    else: 
        print(url, " Is Valid link")

print("Total number of broken links: ", count)