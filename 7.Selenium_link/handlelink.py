from selenium import webdriver 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service(executable_path="/home/harshil/Selenium/Drivers/chromedriver_linux64/chromedriver")

driver = webdriver.Chrome(service = service_obj)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

# click on link
# driver.find_element(By.LINK_TEXT, "Digital downloads").click()


# Find number of links in a page
# links = driver.find_elements(By.TAG_NAME, "a")
# print(len(links))

# print all the link names
# for link in links:
#     print(link.text)