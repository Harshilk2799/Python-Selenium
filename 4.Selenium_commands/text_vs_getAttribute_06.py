from selenium import webdriver 
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://admin-demo.nopcommerce.com/login")


# text = text attribute is used to get text of current element.
# get_attribute_method = get attribute is used to get attributes of an element, such as getting href attribute of anchor tag.



# email_box = driver.find_element(By.XPATH, "//input[@id='Email']")
# email_box.clear()
# email_box.send_keys("admin@gmail.com")
# print("Result of text: ", email_box.text)
# print("Result of get_attribute: ", email_box.get_attribute("value"))


login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
print("Result of text: ", login_button.text)
print("Result of get_attribute: ", login_button.get_attribute("value"))
print("Result of get_attribute: ", login_button.get_attribute("type"))

driver.close()

