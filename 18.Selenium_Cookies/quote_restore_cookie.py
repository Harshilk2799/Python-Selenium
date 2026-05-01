import pickle
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

HOME_URL    = "https://quotes.toscrape.com"
COOKIE_FILE = "session_cookies.pkl"

# Step 1: Start a fresh browser session
driver = webdriver.Chrome()

# IMPORTANT: Must visit the domain first before adding cookies
# Cookies require a matching domain to be loaded
driver.get(HOME_URL)

# Step 2: Load saved cookies and inject them
with open(COOKIE_FILE, "rb")as f:
    saved_cookies = pickle.load(f)

for cookie in saved_cookies:
    # Remove 'expiry' key if present — can cause issues in some drivers
    cookie.pop("expiry", None)
    driver.add_cookie(cookie)

print(f" Injected {len(saved_cookies)} cookies")

# Step 3: Refresh so the browser uses the injected cookies
driver.refresh()

# Step 4: Verify we are already logged in (no login needed!)
wait = WebDriverWait(driver, 10)
logout_link = wait.until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Logout")))

assert logout_link.is_displayed(), "Session restore failed!"
print("Session restored from cookies — logged in without entering password!")

while True:
    quotes = driver.find_elements(By.CSS_SELECTOR, ".quote")
    for quote in quotes:
        title = quote.find_element(By.CSS_SELECTOR, "span.text").text
        author = quote.find_element(By.CSS_SELECTOR, "small.author").text 
        tags = []
        for tag in quote.find_elements(By.CSS_SELECTOR, "a.tag"):
            tags.append(tag.text)
        print("Title: ", title)
        print("Author Name: ", author)
        print("Tags: ", tags)

    try:
        next_button = driver.find_element(By.CSS_SELECTOR, "li.next a")
        if next_button.is_displayed():
            next_button.click()
    except NoSuchElementException:
        break

driver.quit()
