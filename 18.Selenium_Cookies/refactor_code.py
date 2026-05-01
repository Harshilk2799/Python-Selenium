import pickle
from pathlib import Path

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class QuotesCookieManager:
    LOGIN_URL = "https://quotes.toscrape.com/login"
    HOME_URL = "https://quotes.toscrape.com"

    def __init__(self, username, password, cookie_file="session_cookies.pkl", wait_time=10):
        self.username = username
        self.password = password
        self.cookie_file = Path(__file__).parent / cookie_file
        self.wait_time = wait_time
        self.driver = None
        self.wait = None

    def start_browser(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, self.wait_time)

    def close_browser(self):
        if self.driver:
            self.driver.quit()
            self.driver = None
            self.wait = None

    def login_and_store_cookies(self):
        self.start_browser()
        try:
            self.driver.get(self.LOGIN_URL)

            username_field = self.wait.until(
                EC.presence_of_element_located((By.ID, "username"))
            )
            password_field = self.driver.find_element(By.ID, "password")

            username_field.clear()
            username_field.send_keys(self.username)
            password_field.clear()
            password_field.send_keys(self.password)

            submit_button = self.driver.find_element(
                By.CSS_SELECTOR, "input[type='submit']"
            )
            submit_button.click()

            self.wait.until(EC.url_to_be(self.HOME_URL + "/"))
            logout_link = self.wait.until(
                EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Logout"))
            )
            assert logout_link.is_displayed(), "Login failed: Logout link not found."
            print("Login successful!")

            all_cookies = self.driver.get_cookies()
            print(f"\nTotal cookies: {len(all_cookies)}")
            for cookie in all_cookies:
                print(f"Name: {cookie['name']}")
                print(f"Value: {cookie['value']}")
                print(f"Domain: {cookie.get('domain', 'N/A')}")
                print(f"Expires: {cookie.get('expiry', 'Session only')}")
                print("---")

            session_cookie = self.driver.get_cookie("session")
            print(f"\nSession cookie: {session_cookie}")

            with open(self.cookie_file, "wb") as file:
                pickle.dump(all_cookies, file)
            print(f"\nCookies saved to '{self.cookie_file}'")
        finally:
            self.close_browser()

    def restore_session_and_scrape_quotes(self):
        self.start_browser()
        try:
            self.driver.get(self.HOME_URL)

            with open(self.cookie_file, "rb") as file:
                saved_cookies = pickle.load(file)

            for cookie in saved_cookies:
                cookie.pop("expiry", None)
                self.driver.add_cookie(cookie)

            print(f"Injected {len(saved_cookies)} cookies")

            self.driver.refresh()

            logout_link = self.wait.until(
                EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Logout"))
            )
            assert logout_link.is_displayed(), "Session restore failed."
            print("Session restored from cookies. Logged in without entering password!")

            while True:
                quotes = self.driver.find_elements(By.CSS_SELECTOR, ".quote")
                for quote in quotes:
                    title = quote.find_element(By.CSS_SELECTOR, "span.text").text
                    author = quote.find_element(By.CSS_SELECTOR, "small.author").text
                    tags = [
                        tag.text
                        for tag in quote.find_elements(By.CSS_SELECTOR, "a.tag")
                    ]
                    print("Title:", title)
                    print("Author Name:", author)
                    print("Tags:", tags)

                try:
                    next_button = self.driver.find_element(By.CSS_SELECTOR, "li.next a")
                    if next_button.is_displayed():
                        next_button.click()
                except NoSuchElementException:
                    break
        finally:
            self.close_browser()


if __name__ == "__main__":
    USERNAME = "admin"
    PASSWORD = "12345"

    manager = QuotesCookieManager(username=USERNAME, password=PASSWORD)

    # Step 1: Store cookies after login
    # manager.login_and_store_cookies()

    # Step 2: Restore session from saved cookies and scrape quotes
    manager.restore_session_and_scrape_quotes()
