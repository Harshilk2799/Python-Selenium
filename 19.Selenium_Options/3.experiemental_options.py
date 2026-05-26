from selenium import webdriver
from selenium.webdriver import ChromeOptions

options = ChromeOptions()

# Suppress the "Chrome is being controlled by automated software" bar
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)

# Set browser language
options.add_experimental_option("prefs", {
    "intl.accept_languages": "en-US,en"
})

# Detach: keep browser open after script ends (useful for debugging)
# options.add_experimental_option("detach", True)

driver = webdriver.Chrome()
driver.get("https://quotes.toscrape.com")
# Browser stays open after script finishes (due to detach=True)
