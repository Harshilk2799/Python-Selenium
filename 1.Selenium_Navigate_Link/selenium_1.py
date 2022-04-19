from selenium import webdriver
from selenium.webdriver.chrome.service import Service


service_obj = Service("/home/harshil/Selenium/Drivers/chromedriver_linux64/chromedriver")

driver = webdriver.Chrome(service=service_obj)

# Navigating links using get method

# get() = Opening the application URL 
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.close()