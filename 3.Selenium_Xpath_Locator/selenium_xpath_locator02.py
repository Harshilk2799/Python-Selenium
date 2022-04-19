from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By 


service_obj = Service(executable_path="/home/harshil/Selenium/Drivers/chromedriver_linux64/chromedriver")

driver = webdriver.Chrome(service= service_obj)

driver.get("https://money.rediff.com/gainers/bse/daily/groupa")
driver.maximize_window()

# XPATH Axes

# self node
# text_msg = driver.find_element(By.XPATH, "//a[contains(text(), 'Indian Hotels Co')]/self::a").text
# text_msg = driver.find_element(By.XPATH, "//a[normalize-space()='Indian Hotels Co']/self::a").text
# print(text_msg)



# parent node
# text_msg = driver.find_element(By.XPATH, "//a[contains(text(), 'Indian Hotels Co')]/parent::td").text
# print(text_msg)


# child node 
# text_msg = driver.find_element(By.XPATH, "//a[contains(text(), 'Indian Hotels Co')]/ancestor::tr/child::td").text
# print(text_msg)

# child = driver.find_elements(By.XPATH, "//a[contains(text(), 'Indian Hotels Co')]/ancestor::tr/child::td")
# print(len(child))



# ancestor
# text_msg = driver.find_element(By.XPATH, "//a[contains(text(), 'Indian Hotels Co')]/ancestor::tr").text 
# print(text_msg)


# descendant
# descendants = driver.find_elements(By.XPATH, "//a[contains(text(), 'Indian Hotels Co')]/ancestor::tr/descendant::*")
# print("Number of Descendant nodes: ", len(descendants))



# following 
# following = driver.find_elements(By.XPATH, "//a[contains(text(), 'Indian Hotels Co')]/ancestor::tr/following::*")
# print("Number of following nodes: ",len(following))


# following-sibling
# following_sibling = driver.find_elements(By.XPATH, "//a[contains(text(), 'Indian Hotels Co')]/ancestor::tr//following-sibling::*")
# print("Number of following nodes: ",len(following_sibling))




# preceding
# preceding = driver.find_elements(By.XPATH, "//a[contains(text(), 'Indian Hotels Co')]/ancestor::tr/preceding::*")
# print(len(preceding))

# preceding-sibling
preceding_sibling = driver.find_elements(By.XPATH, "//a[contains(text(), 'Indian Hotels Co')]/ancestor::tr/preceding-sibling::*")
print(len(preceding_sibling))
driver.close()