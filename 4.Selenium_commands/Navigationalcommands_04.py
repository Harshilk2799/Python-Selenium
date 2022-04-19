from selenium import webdriver 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service(executable_path="/home/harshil/Selenium/Drivers/chromedriver_linux64/chromedriver")

driver = webdriver.Chrome(service = service_obj)

driver.get("https://demo.nopcommerce.com/register?returnUrl=%2F")
driver.get("https://www.amazon.com")

# back()           = Goes one step backward in the browser history.
# forward()        = Goes one step forward in the browser history.
# refresh()        = Refreshes the current page.




driver.back()  # back to nopcommerce oage
driver.forward()  # go to amazon.com page

driver.refresh()  # refresh the page

driver.quit()