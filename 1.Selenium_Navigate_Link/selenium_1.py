from selenium import webdriver

driver = webdriver.Chrome()

# Navigating links using get method

# get() = Opening the application URL 
driver.get("https://opensource-demo.orangehrmlive.com/")
print(driver.title)
driver.close()