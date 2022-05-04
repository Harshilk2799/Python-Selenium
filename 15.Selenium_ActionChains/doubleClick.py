import time
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


service_obj = Service(executable_path="/home/harshil/Selenium/Drivers/chromedriver_linux64/chromedriver")

driver = webdriver.Chrome(service = service_obj)
driver.implicitly_wait(10)

driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_ev_ondblclick3")
driver.maximize_window()


driver.switch_to.frame("iframeResult")  #Switch to frame 

field1 = driver.find_element(By.ID, "field1")
field1.clear()
field1.send_keys("Welcome!!!")


button = driver.find_element(By.XPATH, "//button[normalize-space()='Copy Text']")

action = ActionChains(driver)

action.double_click(button).perform()  # Double click action


# driver.close()