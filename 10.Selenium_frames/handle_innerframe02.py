from selenium import webdriver 
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("http://demo.automationtesting.in/Frames.html")
driver.maximize_window()


driver.find_element(By.XPATH, "//a[normalize-space()='Iframe with in an Iframe']").click()

outerframe = driver.find_element(By.XPATH, "//iframe[@src='MultipleFrames.html']")
driver.switch_to.frame(outerframe)

innerframe = driver.find_element(By.XPATH, "/html/body/section/div/div/iframe")
driver.switch_to.frame(innerframe)

driver.find_element(By.XPATH, "/html/body/section/div/div/div/input").send_keys("Harshil")

driver.switch_to.parent_frame() # directly switch to parent frame (outerframe)

