from curses import window
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service_obj = Service(executable_path="/home/harshil/Selenium/Drivers/chromedriver_linux64/chromedriver")

driver = webdriver.Chrome(service = service_obj)

driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()

driver.find_element(By.XPATH, "//img[@alt='OrangeHRM on twitter']").click()

# windowID = driver.current_window_handle
# print(windowID)

windowIDs = driver.window_handles
# print(windowIDs)


# Approach 1
# parentwindow = windowIDs[0]
# childwindow = windowIDs[1]

# driver.switch_to.window(childwindow)
# print("Child Window Title: ",driver.title)

# driver.switch_to.window(parentwindow)
# print("Parent Window Title: ",driver.title)

# print(parentwindow)
# print(childwindow)




# Approach 2
# for windowid in windowIDs:
#     driver.switch_to.window(windowid)
#     print(driver.title)



# Which browser has been close you can specified title of the browser
for windowid in windowIDs:
    driver.switch_to.window(windowid)
    if driver.title == "OrangeHRM":
        driver.close()

# driver.close()