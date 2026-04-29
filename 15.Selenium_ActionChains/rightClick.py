import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get("http://swisnl.github.io/jQuery-contextMenu/demo.html")
driver.maximize_window()


button = driver.find_element(By.XPATH, "//span[@class='context-menu-one btn btn-neutral']")

action = ActionChains(driver)

action.context_click(button).perform()


# driver.close()