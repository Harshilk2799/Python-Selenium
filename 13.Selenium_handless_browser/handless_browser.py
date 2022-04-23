from curses import window
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

option = Options()
option.headless = True

# option.add_argument("--incognito")
service_obj = Service(executable_path="/home/harshil/Selenium/Drivers/chromedriver_linux64/chromedriver")

driver = webdriver.Chrome(service = service_obj, options=option)

driver.get("https://whatmylocation.com/")
driver.maximize_window()

print(driver.title)

driver.close()