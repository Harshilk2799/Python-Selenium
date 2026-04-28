from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

option = Options()
option.headless = True

# option.add_argument("--incognito")

driver = webdriver.Chrome(options=option)

driver.get("https://whatmylocation.com/")
driver.maximize_window()

print(driver.title)

driver.close()