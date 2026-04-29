from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys 

driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get("https://text-compare.com/")
driver.maximize_window()


textarea1 = driver.find_element(By.NAME, "text1")
textarea2 = driver.find_element(By.NAME, "text2")

textarea1.send_keys("Hello World")


action = ActionChains(driver)

# input1 ==> Ctrl+A Select all the text
action.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()

# input1  ==> Ctrl+C copy text
action.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()


# Press tab key to navigate to input2
action.key_down(Keys.TAB).perform()


# Input2 ==> Ctrl+V past the text
action.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()

driver.close()