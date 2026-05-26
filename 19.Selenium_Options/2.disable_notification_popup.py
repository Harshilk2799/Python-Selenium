from selenium import webdriver
from selenium.webdriver import ChromeOptions

options = ChromeOptions()

# Disable browser notifications popup
prefs = {
    "profile.default_content_setting_values.notifications": 2,  # 1=allow, 2=block
    "profile.default_content_setting_values.geolocation": 2,    # Block location requests
    "credentials_enable_service": False,                          # Disable password manager
    "profile.password_manager_enabled": False
}
options.add_experimental_option("prefs", prefs)

# Disable extensions
options.add_argument("--disable-extensions")

# Load a specific extension (.crx file)
# options.add_extension("/path/to/extension.crx")

driver = webdriver.Chrome(options=options)
driver.get("https://quotes.toscrape.com/")
driver.quit()