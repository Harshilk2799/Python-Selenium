from selenium import webdriver 

driver = webdriver.Chrome()

driver.get("https://opensource-demo.orangehrmlive.com/")


# print(driver.title)           # To capture the title of the current web page 
# print(driver.current_url)     # To capture the current url of the web page 
# print(driver.page_source)     # To capture source code of the page


driver.close()