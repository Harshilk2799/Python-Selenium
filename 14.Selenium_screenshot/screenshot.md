# Python Selenium Screenshots – Complete Guide

## Introduction

Selenium is a powerful browser automation library for Python. One of its most useful features is the ability to **capture screenshots** of web pages or individual elements during automation. This is invaluable for:

- Debugging test failures
- Visual regression testing
- Documenting UI states
- Monitoring web pages

---

## Installation

```bash
pip install selenium
```

You also need a **WebDriver** matching your browser:

| Browser | WebDriver    |
| ------- | ------------ |
| Chrome  | ChromeDriver |
| Firefox | GeckoDriver  |
| Edge    | EdgeDriver   |

> **Tip:** Use `webdriver-manager` to auto-manage drivers:
>
> ```bash
> pip install webdriver-manager
> ```

---

## 1. Basic Full-Page Screenshot

Capture a screenshot of the entire visible viewport and save it as a `.png` file.

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Setup Chrome driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open a webpage
driver.get("https://www.example.com")

# Take a screenshot and save to file
driver.save_screenshot("full_page_screenshot.png")
print("Screenshot saved!")

driver.quit()
```

**Output:** Saves `full_page_screenshot.png` in the current directory.

---

## 2. Screenshot Using `get_screenshot_as_file()`

An alternative method — functionally identical to `save_screenshot()`, but returns `True`/`False`.

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.python.org")

# Returns True if successful, False otherwise
success = driver.get_screenshot_as_file("python_org.png")

if success:
    print("Screenshot captured successfully!")
else:
    print("Screenshot failed.")

driver.quit()
```

---

## 3. Screenshot as Base64 String

Useful when you want to embed the screenshot in HTML reports or send it over a network without saving to disk.

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import base64

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.example.com")

# Get screenshot as base64-encoded string
screenshot_base64 = driver.get_screenshot_as_base64()

# Embed in an HTML file
html_content = f"""
<html>
  <body>
    <h2>Screenshot Preview</h2>
    <img src="data:image/png;base64,{screenshot_base64}" />
  </body>
</html>
"""

with open("screenshot_preview.html", "w") as f:
    f.write(html_content)

print("HTML with embedded screenshot saved!")
driver.quit()
```

---

## 4. Screenshot as PNG Bytes (In-Memory)

Capture screenshot directly into memory as raw bytes — ideal for processing with libraries like **Pillow**.

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from PIL import Image
import io

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.example.com")

# Get PNG bytes (no file written to disk yet)
png_bytes = driver.get_screenshot_as_png()

# Open with Pillow for processing
image = Image.open(io.BytesIO(png_bytes))

# Resize and save
image_resized = image.resize((800, 600))
image_resized.save("resized_screenshot.png")

print(f"Original size: {image.size}")
print(f"Resized to: {image_resized.size}")
driver.quit()
```

---

## 5. Element Screenshot (Specific Element Only)

Capture only a **specific web element** instead of the full page.

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.python.org")

# Locate a specific element (e.g., the logo)
logo_element = driver.find_element(By.CSS_SELECTOR, ".python-logo")

# Take screenshot of just that element
logo_element.screenshot("logo_only.png")

print("Element screenshot saved!")
driver.quit()
```

> **Note:** The `.screenshot()` method on a WebElement was introduced in Selenium 4.

---

## 6. Timestamped Screenshots

Automatically name screenshots with a timestamp to avoid overwriting.

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.example.com")

# Create timestamp-based filename
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
filename = f"screenshot_{timestamp}.png"

driver.save_screenshot(filename)
print(f"Saved: {filename}")

driver.quit()
```

---

## 7. Screenshot in a Specific Directory

Organize screenshots by saving them into a dedicated folder.

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime
import os

# Create output directory if it doesn't exist
output_dir = "screenshots"
os.makedirs(output_dir, exist_ok=True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.example.com")

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
filepath = os.path.join(output_dir, f"capture_{timestamp}.png")

driver.save_screenshot(filepath)
print(f"Screenshot saved to: {filepath}")

driver.quit()
```

---

## 8. Screenshot on Test Failure (with pytest)

Automatically capture a screenshot whenever a Selenium test fails.

```python
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime
import os

@pytest.fixture
def driver():
    d = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield d
    d.quit()

def take_screenshot_on_failure(driver, test_name):
    os.makedirs("failure_screenshots", exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"failure_screenshots/{test_name}_{timestamp}.png"
    driver.save_screenshot(filename)
    print(f"\n📸 Screenshot saved: {filename}")

def test_page_title(driver):
    try:
        driver.get("https://www.example.com")
        assert "Nonexistent Title" in driver.title, "Title mismatch!"
    except AssertionError as e:
        take_screenshot_on_failure(driver, "test_page_title")
        raise e
```

---

## 9. Full-Page Screenshot (Scrolling Capture)

Selenium captures only the **visible viewport** by default. To capture the full scrollable page, resize the browser window to match the full document height.

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.wikipedia.org")

# Get full page dimensions
total_width  = driver.execute_script("return document.body.scrollWidth")
total_height = driver.execute_script("return document.body.scrollHeight")

# Resize window to full page size
driver.set_window_size(total_width, total_height)

# Now take the screenshot
driver.save_screenshot("full_scrollable_page.png")
print(f"Full page screenshot saved ({total_width}x{total_height}px)")

driver.quit()
```

---

## 10. Headless Browser Screenshot

Capture screenshots **without opening a visible browser window** — perfect for servers and CI/CD pipelines.

```python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Configure headless mode
options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

driver.get("https://www.example.com")
driver.save_screenshot("headless_screenshot.png")
print("Headless screenshot saved!")

driver.quit()
```

---

## Screenshot Methods – Quick Reference

| Method                         | Returns | Saves to Disk | Use Case                      |
| ------------------------------ | ------- | ------------- | ----------------------------- |
| `save_screenshot(path)`        | `bool`  | ✅ Yes        | Standard file save            |
| `get_screenshot_as_file(path)` | `bool`  | ✅ Yes        | Same as above                 |
| `get_screenshot_as_png()`      | `bytes` | ❌ No         | In-memory processing (Pillow) |
| `get_screenshot_as_base64()`   | `str`   | ❌ No         | HTML embedding, API responses |
| `element.screenshot(path)`     | `bool`  | ✅ Yes        | Capture a specific element    |

---

## Best Practices

1. **Always use `driver.quit()`** — closes the browser and frees resources.
2. **Use headless mode** in CI/CD pipelines to avoid GUI dependencies.
3. **Timestamp your filenames** to prevent accidental overwrites.
4. **Capture on failure** to make debugging far easier.
5. **Resize window before full-page captures** to get the full scrollable content.
6. **Store screenshots in a dedicated folder** to keep your project organized.
7. **Use explicit waits** (`WebDriverWait`) before screenshotting to ensure the page is fully loaded.

---

## Common Pitfalls

| Problem                     | Cause                 | Solution                                     |
| --------------------------- | --------------------- | -------------------------------------------- |
| Blank/white screenshot      | Page not fully loaded | Add `time.sleep()` or `WebDriverWait`        |
| Screenshot cuts off content | Viewport too small    | Use `set_window_size()`                      |
| Element screenshot fails    | Selenium < 4          | Upgrade to Selenium 4+                       |
| File not saved              | Invalid path          | Ensure directory exists with `os.makedirs()` |

---

_Guide covers Selenium 4.x with Python 3.x_
