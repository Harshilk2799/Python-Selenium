# Python Selenium Alerts — Complete Guide

## Table of Contents

- [Python Selenium Alerts — Complete Guide](#python-selenium-alerts--complete-guide)
  - [Table of Contents](#table-of-contents)
  - [What Are Alerts?](#what-are-alerts)
  - [Types of Alerts](#types-of-alerts)
  - [Switching to an Alert](#switching-to-an-alert)
    - [Key Alert Methods](#key-alert-methods)
  - [1. Simple Alert](#1-simple-alert)
    - [HTML Example (for testing)](#html-example-for-testing)
    - [Selenium Code](#selenium-code)
    - [Output](#output)
  - [2. Confirmation Alert](#2-confirmation-alert)
    - [HTML Example](#html-example)
    - [Selenium Code — Accepting](#selenium-code--accepting)
    - [Selenium Code — Dismissing](#selenium-code--dismissing)
  - [3. Prompt Alert](#3-prompt-alert)
    - [HTML Example](#html-example-1)
    - [Selenium Code](#selenium-code-1)
    - [Selenium Code — Dismissing a Prompt](#selenium-code--dismissing-a-prompt)
  - [4. Authentication Alert](#4-authentication-alert)
    - [Method 1 — Embed credentials in URL](#method-1--embed-credentials-in-url)
    - [Method 2 — Using `selenium-wire` (captures credentials in headers)](#method-2--using-selenium-wire-captures-credentials-in-headers)
  - [Handling Unexpected Alerts](#handling-unexpected-alerts)
  - [Using WebDriverWait for Alerts](#using-webdriverwait-for-alerts)
  - [Full Working Example (All Alert Types)](#full-working-example-all-alert-types)
    - [Expected Output](#expected-output)
  - [Common Errors \& Fixes](#common-errors--fixes)
  - [Quick Reference Cheat Sheet](#quick-reference-cheat-sheet)
  - [Summary](#summary)

---

## What Are Alerts?

In web browsers, **alerts** are pop-up dialog boxes that interrupt the current page flow and require user interaction before continuing. Selenium provides the `Alert` interface (via `switch_to.alert`) to interact with these dialogs programmatically.

---

## Types of Alerts

| Type                     | Description                | User Actions             |
| ------------------------ | -------------------------- | ------------------------ |
| **Simple Alert**         | Displays a message         | OK                       |
| **Confirmation Alert**   | Asks Yes/No                | OK / Cancel              |
| **Prompt Alert**         | Asks for text input        | Enter text + OK / Cancel |
| **Authentication Alert** | Asks for username/password | Enter credentials        |

---

## Switching to an Alert

Before interacting with any alert, you must switch the WebDriver's focus to it:

```python
alert = driver.switch_to.alert
```

### Key Alert Methods

| Method                    | Description                           |
| ------------------------- | ------------------------------------- |
| `alert.accept()`          | Clicks **OK**                         |
| `alert.dismiss()`         | Clicks **Cancel** or closes the alert |
| `alert.text`              | Gets the alert message text           |
| `alert.send_keys("text")` | Types into a prompt alert             |

---

## 1. Simple Alert

A **simple alert** shows a message and has only an **OK** button.

### HTML Example (for testing)

```html
<button onclick="alert('Hello! This is a simple alert.')">Click Me</button>
```

### Selenium Code

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("your_test_page.html")

# Trigger the alert
driver.find_element(By.TAG_NAME, "button").click()
time.sleep(1)

# Switch to alert
alert = driver.switch_to.alert

# Read alert text
print("Alert message:", alert.text)  # Output: Hello! This is a simple alert.

# Accept (click OK)
alert.accept()

driver.quit()
```

### Output

```
Alert message: Hello! This is a simple alert.
```

---

## 2. Confirmation Alert

A **confirmation alert** presents a message and two buttons: **OK** and **Cancel**.

### HTML Example

```html
<button
  onclick="
  var result = confirm('Do you want to proceed?');
  document.getElementById('result').innerText = result ? 'You clicked OK' : 'You clicked Cancel';
"
>
  Confirm
</button>
<p id="result"></p>
```

### Selenium Code — Accepting

```python
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("your_test_page.html")

driver.find_element(By.TAG_NAME, "button").click()

alert = driver.switch_to.alert
print("Alert text:", alert.text)  # Do you want to proceed?

# Click OK
alert.accept()

result = driver.find_element(By.ID, "result").text
print("Page says:", result)  # You clicked OK

driver.quit()
```

### Selenium Code — Dismissing

```python
driver.find_element(By.TAG_NAME, "button").click()

alert = driver.switch_to.alert
alert.dismiss()  # Click Cancel

result = driver.find_element(By.ID, "result").text
print("Page says:", result)  # You clicked Cancel
```

---

## 3. Prompt Alert

A **prompt alert** has a text input field where the user can type a response.

### HTML Example

```html
<button
  onclick="
  var name = prompt('Please enter your name:');
  document.getElementById('output').innerText = 'Hello, ' + name + '!';
"
>
  Enter Name
</button>
<p id="output"></p>
```

### Selenium Code

```python
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("your_test_page.html")

driver.find_element(By.TAG_NAME, "button").click()

alert = driver.switch_to.alert
print("Prompt message:", alert.text)  # Please enter your name:

# Type text into the prompt
alert.send_keys("Selenium User")

# Click OK
alert.accept()

output = driver.find_element(By.ID, "output").text
print(output)  # Hello, Selenium User!

driver.quit()
```

### Selenium Code — Dismissing a Prompt

```python
driver.find_element(By.TAG_NAME, "button").click()

alert = driver.switch_to.alert
alert.dismiss()  # Click Cancel — no text is submitted
```

---

## 4. Authentication Alert

An **authentication alert** (HTTP Basic Auth dialog) pops up when accessing a protected resource.

### Method 1 — Embed credentials in URL

```python
from selenium import webdriver

driver = webdriver.Chrome()

# Pass credentials directly in the URL
driver.get("https://username:password@the-internet.herokuapp.com/basic_auth")

print(driver.find_element("tag name", "p").text)
# Congratulations! You must have the proper credentials.

driver.quit()
```

### Method 2 — Using `selenium-wire` (captures credentials in headers)

```bash
pip install selenium-wire
```

```python
from seleniumwire import webdriver

options = {
    'proxy': {
        'no_proxy': 'localhost,127.0.0.1'
    }
}

driver = webdriver.Chrome(seleniumwire_options=options)

# Intercept and add Basic Auth header
def interceptor(request):
    import base64
    credentials = base64.b64encode(b"admin:secret").decode("utf-8")
    request.headers['Authorization'] = f'Basic {credentials}'

driver.request_interceptor = interceptor
driver.get("https://protected-site.com/secure")
driver.quit()
```

---

## Handling Unexpected Alerts

Sometimes alerts appear unexpectedly. Use a `try/except` block with `NoAlertPresentException`:

```python
from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException

driver = webdriver.Chrome()
driver.get("https://example.com")

# Perform some action that might trigger an alert
driver.find_element("id", "submit-btn").click()

try:
    alert = driver.switch_to.alert
    print("Unexpected alert found:", alert.text)
    alert.accept()
except NoAlertPresentException:
    print("No alert present, continuing normally.")

driver.quit()
```

---

## Using WebDriverWait for Alerts

Alerts don't always appear instantly. Use **explicit waits** to avoid `NoAlertPresentException`:

```python
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

driver = webdriver.Chrome()
driver.get("your_test_page.html")

driver.find_element("tag name", "button").click()

try:
    # Wait up to 10 seconds for alert to appear
    WebDriverWait(driver, 10).until(EC.alert_is_present())

    alert = driver.switch_to.alert
    print("Alert text:", alert.text)
    alert.accept()
    print("Alert accepted successfully.")

except TimeoutException:
    print("Alert did not appear within 10 seconds.")

driver.quit()
```

---

## Full Working Example (All Alert Types)

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Sample HTML stored inline for demo
html = """
<html><body>
  <button id="simple"  onclick="alert('Simple Alert!')">Simple</button>
  <button id="confirm" onclick="confirm('Are you sure?')">Confirm</button>
  <button id="prompt"  onclick="prompt('Enter your name:')">Prompt</button>
</body></html>
"""

driver = webdriver.Chrome()
driver.get("data:text/html," + html)

wait = WebDriverWait(driver, 5)

# --- Simple Alert ---
driver.find_element(By.ID, "simple").click()
wait.until(EC.alert_is_present())
a = driver.switch_to.alert
print("[Simple]  Text:", a.text)
a.accept()

# --- Confirmation Alert ---
driver.find_element(By.ID, "confirm").click()
wait.until(EC.alert_is_present())
a = driver.switch_to.alert
print("[Confirm] Text:", a.text)
a.dismiss()  # Click Cancel

# --- Prompt Alert ---
driver.find_element(By.ID, "prompt").click()
wait.until(EC.alert_is_present())
a = driver.switch_to.alert
print("[Prompt]  Text:", a.text)
a.send_keys("Alice")
a.accept()

print("All alerts handled!")
driver.quit()
```

### Expected Output

```
[Simple]  Text: Simple Alert!
[Confirm] Text: Are you sure?
[Prompt]  Text: Enter your name:
All alerts handled!
```

---

## Common Errors & Fixes

| Error                              | Cause                                             | Fix                                                          |
| ---------------------------------- | ------------------------------------------------- | ------------------------------------------------------------ |
| `NoAlertPresentException`          | Alert hasn't appeared yet                         | Use `WebDriverWait` + `EC.alert_is_present()`                |
| `UnexpectedAlertPresentException`  | Alert blocks other actions                        | Switch to alert, handle it, then continue                    |
| `ElementClickInterceptedException` | Alert is open when clicking element               | Always dismiss/accept alert before interacting with the page |
| Alert not detected                 | Alert is an HTML modal (not a real browser alert) | Use standard element locators — it's not a real alert        |

---

## Quick Reference Cheat Sheet

```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Wait for alert
WebDriverWait(driver, 10).until(EC.alert_is_present())

# Switch to alert
alert = driver.switch_to.alert

# Get text
print(alert.text)

# Accept (OK)
alert.accept()

# Dismiss (Cancel)
alert.dismiss()

# Send input (Prompt only)
alert.send_keys("your input")
alert.accept()
```

---

## Summary

| Alert Type   | Trigger     | Accept          | Dismiss     | Send Keys       |
| ------------ | ----------- | --------------- | ----------- | --------------- |
| Simple       | `alert()`   | ✅              | ❌          | ❌              |
| Confirmation | `confirm()` | ✅ (OK)         | ✅ (Cancel) | ❌              |
| Prompt       | `prompt()`  | ✅ (OK)         | ✅ (Cancel) | ✅              |
| Auth         | HTTP 401    | Via URL/headers | —           | Via URL/headers |

---

_Generated with Python Selenium — Happy Testing! 🚀_
