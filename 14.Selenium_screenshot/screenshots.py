from selenium import webdriver 

driver = webdriver.Chrome()

driver.get("https://whatmylocation.com/")
driver.maximize_window()

# driver.save_screenshot("website.png")
driver.get_screenshot_as_file("website1.png")

print(driver.title)

driver.close()