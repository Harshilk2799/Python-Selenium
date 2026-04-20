from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
# from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

# Navigating links using get method

# get() = Opening the application URL 
driver.get("https://opensource-demo.orangehrmlive.com/")
print(driver.title)
driver.close()