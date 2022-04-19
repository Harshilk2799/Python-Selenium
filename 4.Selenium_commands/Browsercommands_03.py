from selenium import webdriver 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service_obj = Service(executable_path="/home/harshil/Selenium/Drivers/chromedriver_linux64/chromedriver")

driver = webdriver.Chrome(service = service_obj)

driver.get("https://opensource-demo.orangehrmlive.com/")

# close() and quit()

# close()  = close the current window.(close single browser window. where driver focused)
# quit()   = quits the driver and closes every associated window. 

driver.maximize_window()

driver.find_element(By.LINK_TEXT, "OrangeHRM, Inc").click()

time.sleep(4)

# driver.close()
driver.quit()