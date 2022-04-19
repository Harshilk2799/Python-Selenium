from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


service_obj = Service("/home/harshil/Selenium/Drivers/chromedriver_linux64/chromedriver")

driver = webdriver.Chrome(service=service_obj)

driver.get("http://automationpractice.com/index.php")
driver.maximize_window()    # maximize window

# CLASS_NAME and TAG_NAME Locators

# slider = driver.find_elements(By.CLASS_NAME, "homeslider-container")
# print(len(slider))  # total number of slider in home page


links = driver.find_elements(By.TAG_NAME, "a")
print(len(links))    # total number of links in home page                   

driver.close()
# driver.quit()