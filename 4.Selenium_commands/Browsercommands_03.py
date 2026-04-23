from selenium import webdriver 
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://opensource-demo.orangehrmlive.com/")

# close() and quit()

# close()  = close the current window.(close single browser window. where driver focused)
# quit()   = quits the driver and closes every associated window. 

driver.maximize_window()

driver.find_element(By.LINK_TEXT, "OrangeHRM, Inc").click()

time.sleep(4)

# driver.close()
driver.quit()