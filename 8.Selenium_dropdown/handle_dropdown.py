from selenium import webdriver 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service(executable_path="/home/harshil/Selenium/Drivers/chromedriver_linux64/chromedriver")

driver = webdriver.Chrome(service = service_obj)

driver.get("https://www.opencart.com/index.php?route=account/register")
driver.maximize_window()

# dropdown_country = driver.find_element(By.XPATH, "//select[@id='input-country']")
dropdown_country = Select(driver.find_element(By.XPATH, "//select[@id='input-country']"))

# Select option from the dropdown

# Method 1
# dropdown_country.select_by_visible_text("India")

# Method 2
# dropdown_country.select_by_value("13")

# Method 3
# dropdown_country.select_by_index(14)


# Capture all the options and print them.
# alloptions = dropdown_country.options
# print("Total Number of Options: ", len(alloptions))

# for alloption in alloptions:
#     print(alloption.text)




# Select option from dropdown without using built-in method 
alloptions = dropdown_country.options

for option in alloptions:
    if option.text == "India":
        option.click()
        break