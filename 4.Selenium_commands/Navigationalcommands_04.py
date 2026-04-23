from selenium import webdriver 
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://demo.nopcommerce.com/register?returnUrl=%2F")
driver.get("https://www.amazon.com")

# back()           = Goes one step backward in the browser history.
# forward()        = Goes one step forward in the browser history.
# refresh()        = Refreshes the current page.




driver.back()  # back to nopcommerce oage
driver.forward()  # go to amazon.com page

driver.refresh()  # refresh the page

driver.quit()