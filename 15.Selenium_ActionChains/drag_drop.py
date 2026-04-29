import time
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
driver.maximize_window()

source_element = driver.find_element(By.ID, "box6")
target_element = driver.find_element(By.ID, "box106")

action = ActionChains(driver)

action.drag_and_drop(source_element, target_element).perform() #Drag and Drop Operation


# driver.close()