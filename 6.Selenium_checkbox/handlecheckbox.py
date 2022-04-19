from selenium import webdriver 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service_obj = Service(executable_path="/home/harshil/Selenium/Drivers/chromedriver_linux64/chromedriver")

driver = webdriver.Chrome(service = service_obj)

driver.get("https://itera-qa.azurewebsites.net/home/automation")
driver.maximize_window()

# 1. select specific checkbox 
# driver.find_element(By.XPATH, "//label[normalize-space()='Monday']").click()


# 2. select all the checkbox 
# checkboxes = driver.find_elements(By.XPATH,"//input[@type='checkbox' and contains(@id, 'day')]")
# print(len(checkboxs))

# Approach 1
# for i in range(len(checkboxes)):
#     checkboxs[i].click()

# Approach 2
# for checkbox in checkboxes:
#     checkbox.click()



# 3.Select multiple checkboxs by choice 
# checkboxes = driver.find_elements(By.XPATH,"//input[@type='checkbox' and contains(@id, 'day')]")

# for checkbox in checkboxes:
#     weekname = checkbox.get_attribute("id")
#     if weekname == "monday" or weekname == "sunday":
#         checkbox.click()


# 4. select last 2 checkbox
# checkboxes = driver.find_elements(By.XPATH,"//input[@type='checkbox' and contains(@id, 'day')]")

# # totalnumberof element - how many element you want
# for i in range(len(checkboxes)-2, len(checkboxes)):
#     checkboxs[i].click()


# 5. select first 2 checkbox
# checkboxes = driver.find_elements(By.XPATH,"//input[@type='checkbox' and contains(@id, 'day')]")

# for i in range(len(checkboxes)):
#     if i < 2:
#         checkboxs[i].click()


# 6. Clearning all the checkboxes
checkboxes = driver.find_elements(By.XPATH,"//input[@type='checkbox' and contains(@id, 'day')]")


for checkbox in checkboxes:
    checkbox.click()

time.sleep(5)

for checkbox in checkboxes:
    if checkbox.is_selected():
        checkbox.click()