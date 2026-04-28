from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

option = Options()
option.add_argument("--disable-notification")

driver = webdriver.Chrome(options=option)

driver.get("https://whatmylocation.com/")
driver.maximize_window()

driver.close()