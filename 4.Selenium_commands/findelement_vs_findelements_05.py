from selenium import webdriver 
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://demo.nopcommerce.com/")


#1. find_element() = Returns single web element
# =====================================================


# 1. Locator matching with single webelement
# element = driver.find_element(By.XPATH, "//input[@id='small-searchterms']")
# element.send_keys("Apple MacBook Pro")


# 2. Locator matching with multiple webelements
# a_link = driver.find_element(By.XPATH, "//div[@class='footer']//a")
# print(a_link.text)
# print(a_link.get_attribute("href"))


# 3. Element not available then throw NoSuchElementException
# login_ = driver.find_element(By.LINK_TEXT, "Log In")
# login_.click()






# 2. find_elements() = Returns multiple web elements
# ============================================================


# 1. Locator matching with single webelement
# elements = driver.find_elements(By.XPATH, "//input[@id='small-searchterms']") # return list of webelements
# print(len(elements)) 
# elements[0].send_keys("Apple MacBook Pro")




# 2. Locator matching with multiple webelements
# a_links = driver.find_elements(By.XPATH, "//div[@class='footer']//a")
# print(len(a_links))

# print(a_links[0].text)
# for a_link in a_links:
#     print(a_link.text)
#     print(a_link.get_attribute("href"))




# 3. Element not available no exception has thrown return zero value
login_ = driver.find_elements(By.LINK_TEXT, "Log")
print(len(login_))


driver.close()