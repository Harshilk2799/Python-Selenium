# Selenium Options in Python — Complete Guide

## Table of Contents

1. [What Are Selenium Options?](#what-are-selenium-options)
2. [ChromeOptions](#chromeoptions)
3. [FirefoxOptions](#firefoxoptions)
4. [EdgeOptions](#edgeoptions)
5. [Common Options & Arguments](#common-options--arguments)
6. [Headless Mode](#headless-mode)
7. [Handling SSL & Security](#handling-ssl--security)
8. [Setting Download Directory](#setting-download-directory)
9. [Proxy Configuration](#proxy-configuration)
10. [Disabling Extensions & Notifications](#disabling-extensions--notifications)
11. [Mobile Emulation (Chrome)](#mobile-emulation-chrome)
12. [Experimental Options (Chrome)](#experimental-options-chrome)
13. [Capabilities vs Options](#capabilities-vs-options)
14. [Full Real-World Example](#full-real-world-example)

---

## What Are Selenium Options?

Selenium **Options** classes allow you to configure how a browser is launched and how it behaves during automation. You can control things like:

- Running browsers in headless mode (no GUI)
- Ignoring SSL errors
- Setting download directories
- Emulating mobile devices
- Disabling notifications or extensions

Each browser has its own Options class:

| Browser | Options Class    | Import                                          |
| ------- | ---------------- | ----------------------------------------------- |
| Chrome  | `ChromeOptions`  | `from selenium.webdriver import ChromeOptions`  |
| Firefox | `FirefoxOptions` | `from selenium.webdriver import FirefoxOptions` |
| Edge    | `EdgeOptions`    | `from selenium.webdriver import EdgeOptions`    |

---

## ChromeOptions

```python
from selenium import webdriver
from selenium.webdriver import ChromeOptions

options = ChromeOptions()

# Add arguments
options.add_argument("--headless")           # Run without UI
options.add_argument("--no-sandbox")         # Required in some CI environments
options.add_argument("--disable-gpu")        # Disable GPU acceleration
options.add_argument("--window-size=1920,1080")  # Set window size

# Launch Chrome with options
driver = webdriver.Chrome(options=options)
driver.get("https://example.com")
print(driver.title)
driver.quit()
```

---

## FirefoxOptions

```python
from selenium import webdriver
from selenium.webdriver import FirefoxOptions

options = FirefoxOptions()

# Add arguments
options.add_argument("--headless")
options.add_argument("--width=1920")
options.add_argument("--height=1080")

# Set Firefox preferences
options.set_preference("browser.download.folderList", 2)
options.set_preference("browser.download.dir", "/tmp/downloads")
options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/pdf")

driver = webdriver.Firefox(options=options)
driver.get("https://example.com")
print(driver.title)
driver.quit()
```

---

## EdgeOptions

```python
from selenium import webdriver
from selenium.webdriver import EdgeOptions

options = EdgeOptions()

options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")

driver = webdriver.Edge(options=options)
driver.get("https://example.com")
print(driver.title)
driver.quit()
```

---

## Common Options & Arguments

These arguments are widely used across Chrome and Edge (Chromium-based):

```python
from selenium import webdriver
from selenium.webdriver import ChromeOptions

options = ChromeOptions()

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
options.add_argument("--ignore-certificate-errors")
options.add_argument("--allow-running-insecure-content")
options.add_argument("--disable-web-security")

# ----- Automation Detection -----
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)

driver = webdriver.Chrome(options=options)
```

---

## Headless Mode

Headless mode runs the browser without opening a visible window — perfect for servers and CI/CD pipelines.

```python
from selenium import webdriver
from selenium.webdriver import ChromeOptions

options = ChromeOptions()

# Modern headless (recommended for Chrome >= 112)
options.add_argument("--headless=new")

# Legacy headless (older Chrome versions)
# options.add_argument("--headless")

options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource in Docker
options.add_argument("--window-size=1920,1080")  # Important: set size in headless mode

driver = webdriver.Chrome(options=options)
driver.get("https://example.com")

# Take a screenshot to verify
driver.save_screenshot("screenshot.png")
print(f"Page title: {driver.title}")

driver.quit()
```

> **Tip:** Always set `--window-size` in headless mode. Without it, the viewport defaults to a very small size, which can break responsive layouts.

---

## Handling SSL & Security

```python
from selenium import webdriver
from selenium.webdriver import ChromeOptions

options = ChromeOptions()

# Ignore SSL certificate errors (useful for test environments)
options.add_argument("--ignore-certificate-errors")
options.add_argument("--ignore-ssl-errors")

# Accept insecure certificates via capabilities
options.accept_insecure_certs = True

driver = webdriver.Chrome(options=options)
driver.get("https://self-signed.badssl.com/")
print(driver.title)  # Should load without SSL warning
driver.quit()
```

---

## Setting Download Directory

### Chrome

```python
from selenium import webdriver
from selenium.webdriver import ChromeOptions
import os

download_path = os.path.abspath("./downloads")
os.makedirs(download_path, exist_ok=True)

options = ChromeOptions()

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
driver.get("https://example.com/some-file.pdf")
# File will auto-download to ./downloads/
driver.quit()
```

### Firefox

```python
from selenium import webdriver
from selenium.webdriver import FirefoxOptions

options = FirefoxOptions()

options.set_preference("browser.download.folderList", 2)          # Use custom folder
options.set_preference("browser.download.dir", "/tmp/downloads")
options.set_preference("browser.download.useDownloadDir", True)
options.set_preference("browser.helperApps.neverAsk.saveToDisk",
                       "application/pdf,application/zip,text/csv")

driver = webdriver.Firefox(options=options)
```

---

## Proxy Configuration

```python
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.proxy import Proxy, ProxyType

# ---- Method 1: Direct argument ----
options = ChromeOptions()
options.add_argument("--proxy-server=http://proxy_host:8080")

# ---- Method 2: Proxy object ----
proxy = Proxy()
proxy.proxy_type = ProxyType.MANUAL
proxy.http_proxy = "proxy_host:8080"
proxy.ssl_proxy  = "proxy_host:8080"

options = ChromeOptions()
options.proxy = proxy

# ---- Method 3: SOCKS5 proxy ----
options = ChromeOptions()
options.add_argument("--proxy-server=socks5://127.0.0.1:1080")

driver = webdriver.Chrome(options=options)
driver.get("https://example.com")
driver.quit()
```

---

## Disabling Extensions & Notifications

```python
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
driver.get("https://example.com")
driver.quit()
```

---

## Mobile Emulation (Chrome)

```python
from selenium import webdriver
from selenium.webdriver import ChromeOptions

options = ChromeOptions()

# ---- Method 1: Emulate a named device ----
mobile_emulation = {"deviceName": "iPhone 12 Pro"}
options.add_experimental_option("mobileEmulation", mobile_emulation)

# ---- Method 2: Custom device metrics ----
mobile_emulation = {
    "deviceMetrics": {
        "width": 390,
        "height": 844,
        "pixelRatio": 3.0,
        "touch": True
    },
    "userAgent": (
        "Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) "
        "AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1"
    )
}
options.add_experimental_option("mobileEmulation", mobile_emulation)

driver = webdriver.Chrome(options=options)
driver.get("https://example.com")

# Get current window size to verify
size = driver.get_window_size()
print(f"Width: {size['width']}, Height: {size['height']}")

driver.quit()
```

**Supported device names include:**

- `"iPhone 12 Pro"`, `"iPhone SE"`, `"Pixel 5"`
- `"iPad"`, `"iPad Mini"`, `"Galaxy S20 Ultra"`
- `"Nexus 5"`, `"Kindle Fire HDX"`

---

## Experimental Options (Chrome)

Experimental options use `add_experimental_option()` and are passed as Chrome preferences:

```python
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
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.get("https://example.com")
# Browser stays open after script finishes (due to detach=True)
```

---

## Capabilities vs Options

In older Selenium (< 4), you used `DesiredCapabilities`. In **Selenium 4+**, use `Options` instead — they merge capabilities internally.

```python
# ❌ Old way (Selenium 3) — Deprecated
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
caps = DesiredCapabilities.CHROME.copy()
caps["goog:loggingPrefs"] = {"performance": "ALL"}

# ✅ New way (Selenium 4+) — Recommended
from selenium.webdriver import ChromeOptions

options = ChromeOptions()
options.set_capability("goog:loggingPrefs", {"performance": "ALL"})

driver = webdriver.Chrome(options=options)

# Get browser performance logs
logs = driver.get_log("performance")
for entry in logs[:5]:
    print(entry)

driver.quit()
```

---

## Full Real-World Example

A complete script demonstrating multiple options together for a reliable scraping setup:

```python
"""
Full Selenium Options Example
-------------------------------
Demonstrates: headless, anti-detection, no notifications,
custom window size, download dir, SSL bypass, and mobile emulation.
"""

from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time


def get_driver(headless: bool = True, mobile: bool = False) -> webdriver.Chrome:
    """
    Returns a configured Chrome WebDriver instance.

    Args:
        headless: Run without a visible browser window.
        mobile: Emulate iPhone 12 Pro screen.
    """
    options = ChromeOptions()

    # ── Headless ────────────────────────────────────────────
    if headless:
        options.add_argument("--headless=new")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

    # ── Window & Display ────────────────────────────────────
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--start-maximized")

    # ── Anti-Detection ──────────────────────────────────────
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)

    # ── Security ────────────────────────────────────────────
    options.add_argument("--ignore-certificate-errors")
    options.accept_insecure_certs = True

    # ── Performance ─────────────────────────────────────────
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-plugins-discovery")

    # ── Notifications & Popups ──────────────────────────────
    prefs = {
        "profile.default_content_setting_values.notifications": 2,
        "profile.default_content_setting_values.geolocation": 2,
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        # Download settings
        "download.default_directory": os.path.abspath("./downloads"),
        "download.prompt_for_download": False,
        "plugins.always_open_pdf_externally": True,
    }
    options.add_experimental_option("prefs", prefs)

    # ── Mobile Emulation ────────────────────────────────────
    if mobile:
        options.add_experimental_option(
            "mobileEmulation", {"deviceName": "iPhone 12 Pro"}
        )

    driver = webdriver.Chrome(options=options)

    # Override navigator.webdriver to reduce bot detection
    driver.execute_script(
        "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"
    )

    return driver


def scrape_example():
    driver = get_driver(headless=True)
    wait = WebDriverWait(driver, 10)

    try:
        driver.get("https://quotes.toscrape.com/")

        # Wait for quotes to load
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "quote")))

        quotes = driver.find_elements(By.CLASS_NAME, "quote")

        print(f"Found {len(quotes)} quotes on the page:\n")
        for i, quote in enumerate(quotes[:3], 1):
            text   = quote.find_element(By.CLASS_NAME, "text").text
            author = quote.find_element(By.CLASS_NAME, "author").text
            print(f"  {i}. {text}")
            print(f"     — {author}\n")

    finally:
        driver.quit()


if __name__ == "__main__":
    scrape_example()
```

**Expected Output:**

```
Found 10 quotes on the page:

  1. "The world as we have created it is a process of our thinking..."
     — Albert Einstein

  2. "It is our choices, Harry, that show what we truly are..."
     — J.K. Rowling

  3. "There are only two ways to live your life..."
     — Albert Einstein
```

---

## Quick Reference Cheat Sheet

| Goal                  | Code                                                                                  |
| --------------------- | ------------------------------------------------------------------------------------- |
| Headless mode         | `options.add_argument("--headless=new")`                                              |
| Ignore SSL errors     | `options.add_argument("--ignore-certificate-errors")`                                 |
| Maximize window       | `options.add_argument("--start-maximized")`                                           |
| Disable notifications | `prefs["profile.default_content_setting_values.notifications"] = 2`                   |
| Block images          | `options.add_argument("--blink-settings=imagesEnabled=false")`                        |
| Mobile emulation      | `options.add_experimental_option("mobileEmulation", {"deviceName": "iPhone 12 Pro"})` |
| Custom download dir   | `prefs["download.default_directory"] = "/path/to/dir"`                                |
| Anti-bot detection    | `options.add_argument("--disable-blink-features=AutomationControlled")`               |
| Keep browser open     | `options.add_experimental_option("detach", True)`                                     |
| Set proxy             | `options.add_argument("--proxy-server=http://host:port")`                             |

---

_Generated with Python · Selenium 4.x · Last updated: 2026_
