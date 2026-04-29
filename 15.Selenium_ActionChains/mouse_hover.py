import time
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()

driver.get("https://opensource-demo.orangehrmlive.com/")


driver.find_element(By.ID, "txtUsername").send_keys("Admin")
driver.find_element(By.ID, "txtPassword").send_keys("admin123")
driver.find_element(By.ID, "btnLogin").click()
time.sleep(4)


admin_menu = driver.find_element(By.XPATH, "//li/a[@id='menu_admin_viewAdminModule']/b")
usermanager_menu = driver.find_element(By.XPATH, "//li/a[@id='menu_admin_UserManagement']")
users_menu = driver.find_element(By.XPATH, "//li/a[@id='menu_admin_viewSystemUsers']")

action = ActionChains(driver)

action.move_to_element(admin_menu).move_to_element(usermanager_menu).move_to_element(users_menu).click().perform()


# driver.close()

# 