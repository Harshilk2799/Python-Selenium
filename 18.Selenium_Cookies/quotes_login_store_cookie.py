import pickle
import time 
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 


# Config
LOGIN_URL  = "https://quotes.toscrape.com/login"
HOME_URL   = "https://quotes.toscrape.com"
USERNAME   = "admin"
PASSWORD   = "12345"
COOKIE_FILE = "session_cookies.pkl"

driver = webdriver.Chrome()
driver.get(LOGIN_URL)

wait = WebDriverWait(driver, 10)

username_field = wait.until(EC.presence_of_element_located((By.ID, "username")))
password_field = driver.find_element(By.ID, "password")

username_field.clear()
username_field.send_keys(USERNAME)
password_field.clear()
password_field.send_keys(PASSWORD)

submit_button = driver.find_element(By.CSS_SELECTOR, "input[type='submit']")
submit_button.click()

# Verify login succeeded
wait.until(EC.url_to_be(HOME_URL + "/"))

# Check the logout link appears
logout_link = wait.until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Logout")))
assert logout_link.is_displayed(), "Login failed — Logout link not found!"
print("Login successful!")

# Read and print all cookies
all_cookies = driver.get_cookies()
print(f"\n Total cookies: {len(all_cookies)}")
for cookie in all_cookies:
    print(f"  Name : {cookie['name']}")
    print(f"  Value: {cookie['value']}")
    print(f"  Domain: {cookie.get('domain', 'N/A')}")
    print(f"  Expires: {cookie.get('expiry', 'Session only')}")
    print("  ---")

# Get a specific cookie
session_cookie = driver.get_cookie("session")
print(f"\n Session cookie: {session_cookie}")

# Save cookies to a file
with open(COOKIE_FILE, "wb") as f:
    pickle.dump(driver.get_cookies(), f)
    print(f"\n Cookies saved to '{COOKIE_FILE}'")

driver.quit()
