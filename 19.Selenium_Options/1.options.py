from selenium.webdriver import ChromeOptions
from selenium import webdriver
import os


options = ChromeOptions()

# Add arguments
# options.add_argument("--no-sandbox")    # Required in some CI environments
# options.add_argument("--disable-gpu")        # Disable GPU acceleration

# ----- Display -----
options.add_argument("--start-maximized")       # Maximize window on start
options.add_argument("--window-size=1366,768")  # Set specific window size
options.add_argument("--kiosk")                 # Full-screen kiosk mode

# ----- Performance -----
options.add_argument("--disable-extensions")    # Disable all extensions
options.add_argument("--disable-plugins")       # Disable plugins
options.add_argument("--disable-images")        # Block image loading (faster)
options.add_argument("--blink-settings=imagesEnabled=false")  # Alternative image block

# ----- Security -----
# Ignore SSL certificate errors (useful for test environments
options.add_argument("--ignore-certificate-errors")
options.add_argument("--allow-running-insecure-content")
options.add_argument("--disable-web-security")

# Accept insecure certificates via capabilities
# options.accept_insecure_certs = True

# ----- Automation Detection -----
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)


# Modern headless (recommended for Chrome >= 112)
options.add_argument("--headless=new")
options.add_argument("--window-size=1920,1080")  # Important: set size in headless mode

# Legacy headless (older Chrome versions)
# options.add_argument("--headless")


# Setting Download Directory
download_path = os.path.abspath("./downloads")
os.makedirs(download_path, exist_ok=True)

# Set download preferences
prefs = {
    "download.default_directory": download_path,
    "download.prompt_for_download": False,       # Don't ask where to save
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True,                # Allow downloads without warnings
    "plugins.always_open_pdf_externally": True   # Download PDFs instead of previewing
}
options.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome(options=options)

# Launch Chrome with options
driver = webdriver.Chrome(options=options)
driver.get("https://quotes.toscrape.com/")
print(driver.title)
driver.quit()