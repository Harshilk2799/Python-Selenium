from curses import window
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


service_obj = Service(executable_path="/home/harshil/Selenium/Drivers/chromedriver_linux64/chromedriver")

driver = webdriver.Chrome(service = service_obj)

driver.get("https://whatmylocation.com/")
driver.maximize_window()

# driver.save_screenshot("website.png")
driver.get_screenshot_as_file("website1.png")

print(driver.title)

driver.close()