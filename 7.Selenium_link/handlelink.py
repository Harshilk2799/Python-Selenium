from selenium import webdriver 
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

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