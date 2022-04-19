from selenium import webdriver 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By 
import time
# from webdriver_manager.chrome import ChromeDriverManager

# driver = webdriver.Chrome(ChromeDriverManager().install())

service_obj = Service("/home/harshil/Selenium/Drivers/chromedriver_linux64/chromedriver")

driver = webdriver.Chrome(service=service_obj)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()


# Absolute Path 
# driver.find_element(By.XPATH, "/html/body/div[6]/div[1]/div[2]/div[2]/form/input").send_keys("T-shirts")
# driver.find_element(By.XPATH, "/html/body/div[6]/div[1]/div[2]/div[2]/form/button").click()

# Relative Path
# driver.find_element(By.XPATH, "//*[@id='small-searchterms']").send_keys("T-shirts")
# driver.find_element(By.XPATH, "//*[@id='small-search-box-form']/button").click()

# XPath with or 
# driver.find_element(By.XPATH, "//*[@id='small-searchterms' or @name='q']").send_keys("T-shirts")
# driver.find_element(By.XPATH, "//*[@id='small-search-box-form']/button").click()


# XPath with And 
# driver.find_element(By.XPATH, "//*[@id='small-searchterms' and @name='q']").send_keys("T-shirts")
# driver.find_element(By.XPATH, "//*[@id='small-search-box-form']/button").click()

# XPath with contains and starts-with
driver.find_element(By.XPATH, "//*[contains(@id, 'small-searchterms')]").send_keys("T-shirts")
driver.find_element(By.XPATH, "//*[starts-with(@class, 'button-1 search-box')]").click()

# XPath with text()
# data = driver.find_element(By.XPATH, "//button[text() = 'Search']")
# print(data)

time.sleep(5)

driver.close()
