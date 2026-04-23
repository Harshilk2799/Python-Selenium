# Python Selenium – Complete Guide

Selenium is a powerful open-source framework for automating web browsers. With Python bindings, it allows you to programmatically control browsers like Chrome, Firefox, and Edge — enabling tasks such as web scraping, automated testing, and UI interaction simulation.

---

## Table of Contents

- [Python Selenium – Complete Guide](#python-selenium--complete-guide)
  - [Table of Contents](#table-of-contents)
  - [Installation \& Setup](#installation--setup)
  - [Basic Browser Attributes](#basic-browser-attributes)
    - [`title`](#title)
    - [`current_url`](#current_url)
    - [`page_source`](#page_source)
  - [Browser Control Methods](#browser-control-methods)
    - [`close()`](#close)
    - [`quit()`](#quit)
  - [Finding Elements](#finding-elements)
    - [`find_element()`](#find_element)
    - [`find_elements()`](#find_elements)
  - [Element State Methods](#element-state-methods)
    - [`is_displayed()`](#is_displayed)
    - [`is_enabled()`](#is_enabled)
    - [`is_selected()`](#is_selected)
  - [Navigation Methods](#navigation-methods)
    - [`back()`](#back)
    - [`forward()`](#forward)
    - [`refresh()`](#refresh)
  - [Element Content \& Attributes](#element-content--attributes)
    - [`text`](#text)
    - [`get_attribute()`](#get_attribute)
  - [Full Example Script](#full-example-script)
  - [Quick Reference Cheat Sheet](#quick-reference-cheat-sheet)

---

## Installation & Setup

```bash
pip install selenium
```

You also need a browser driver (e.g., ChromeDriver for Chrome):

```bash
pip install webdriver-manager
```

**Basic setup:**

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.example.com")
```

---

## Basic Browser Attributes

### `title`

Returns the title of the current web page (the `<title>` tag content).

```python
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.wikipedia.org")

print(driver.title)
# Output: Wikipedia
```

**Use case:** Verify navigation by asserting the page title during tests.

---

### `current_url`

Returns the full URL of the currently loaded page as a string.

```python
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.google.com")

print(driver.current_url)
# Output: https://www.google.com/

# After interacting/redirecting:
driver.get("https://www.google.com/search?q=selenium")
print(driver.current_url)
# Output: https://www.google.com/search?q=selenium
```

**Use case:** Confirm redirects, URL changes after form submissions, or login flows.

---

### `page_source`

Returns the complete HTML source code of the current page as a string.

```python
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.example.com")

html = driver.page_source
print(html[:500])  # Print first 500 characters
# Output: <!doctype html><html><head><title>Example Domain</title>...
```

**Use case:** Web scraping, debugging layout issues, or checking if dynamic content has loaded.

---

## Browser Control Methods

### `close()`

Closes the **current browser window or tab** that is in focus. If only one tab is open, it closes the browser window but the WebDriver session remains active.

```python
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.example.com")

# Open a new tab
driver.execute_script("window.open('https://www.google.com', '_blank');")
driver.switch_to.window(driver.window_handles[1])  # Switch to new tab

driver.close()  # Closes only the current (second) tab
# The WebDriver session is still alive; first tab remains open
```

> ⚠️ After `close()`, if no windows remain, you must call `quit()` to clean up the session.

---

### `quit()`

Closes **all browser windows** and terminates the WebDriver session completely. Always use this to avoid memory leaks and dangling browser processes.

```python
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.example.com")

driver.quit()  # Closes all windows and ends the session
# driver is now invalid; any further calls will raise an error
```

**Key Difference:**

| Method    | Closes             | Ends Session |
| --------- | ------------------ | ------------ |
| `close()` | Current tab/window | No           |
| `quit()`  | All tabs/windows   | Yes          |

---

## Finding Elements

Selenium uses `By` locators to identify elements on the page.

```python
from selenium.webdriver.common.by import By
```

**Available locators:**

| Locator                | Description                  |
| ---------------------- | ---------------------------- |
| `By.ID`                | Matches element by `id`      |
| `By.NAME`              | Matches element by `name`    |
| `By.CLASS_NAME`        | Matches element by class     |
| `By.TAG_NAME`          | Matches by HTML tag          |
| `By.LINK_TEXT`         | Full text of an `<a>` tag    |
| `By.PARTIAL_LINK_TEXT` | Partial text of an `<a>` tag |
| `By.CSS_SELECTOR`      | CSS selector syntax          |
| `By.XPATH`             | XPath expression             |

---

### `find_element()`

Returns the **first matching element** as a `WebElement` object. Raises `NoSuchElementException` if no match is found.

```python
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.google.com")

# Find by NAME
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Selenium Python")

# Find by ID
element = driver.find_element(By.ID, "main-header")

# Find by CSS Selector
button = driver.find_element(By.CSS_SELECTOR, "button.submit-btn")

# Find by XPath
link = driver.find_element(By.XPATH, "//a[@href='/about']")
```

---

### `find_elements()`

Returns a **list of all matching elements**. Returns an **empty list** (not an exception) if no elements are found.

```python
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.example.com")

# Find all links on the page
links = driver.find_elements(By.TAG_NAME, "a")
for link in links:
    print(link.text, "->", link.get_attribute("href"))

# Find all items with a specific class
items = driver.find_elements(By.CLASS_NAME, "product-card")
print(f"Found {len(items)} product cards")

# Find all checkboxes
checkboxes = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")
```

**Key Difference:**

| Method            | Returns             | If Not Found       |
| ----------------- | ------------------- | ------------------ |
| `find_element()`  | Single `WebElement` | Raises exception   |
| `find_elements()` | List of elements    | Returns empty list |

---

## Element State Methods

### `is_displayed()`

Returns `True` if the element is **visible** on the page (not hidden by CSS, `display: none`, `visibility: hidden`, etc.).

```python
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.example.com")

banner = driver.find_element(By.ID, "notification-banner")

if banner.is_displayed():
    print("Banner is visible to the user")
else:
    print("Banner is hidden")
```

**Use case:** Verify modals, tooltips, dropdowns, or error messages appear/disappear correctly.

---

### `is_enabled()`

Returns `True` if the element is **interactive** (not disabled). Useful for buttons, inputs, and form fields.

```python
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.example.com/form")

submit_btn = driver.find_element(By.ID, "submit-button")

if submit_btn.is_enabled():
    submit_btn.click()
    print("Button clicked")
else:
    print("Button is disabled — cannot click")
```

**Use case:** Ensure form validation enables/disables the submit button correctly.

---

### `is_selected()`

Returns `True` if the element is **currently selected**. Applies to checkboxes, radio buttons, and `<option>` elements in dropdowns.

```python
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.example.com/settings")

checkbox = driver.find_element(By.ID, "newsletter-checkbox")

print(f"Selected: {checkbox.is_selected()}")  # False

checkbox.click()  # Toggle it

print(f"Selected: {checkbox.is_selected()}")  # True
```

**Use case:** Verify checkbox states before or after interaction; validate that a specific radio option is pre-selected.

---

## Navigation Methods

### `back()`

Simulates clicking the browser's **Back button** — navigates to the previous page in the session history.

```python
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.google.com")
driver.get("https://www.wikipedia.org")

print(driver.title)  # Wikipedia

driver.back()

print(driver.title)  # Google
```

---

### `forward()`

Simulates clicking the browser's **Forward button** — navigates to the next page in the session history.

```python
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.google.com")
driver.get("https://www.wikipedia.org")

driver.back()
print(driver.title)  # Google

driver.forward()
print(driver.title)  # Wikipedia
```

---

### `refresh()`

Simulates pressing **F5** or clicking the browser's Reload button — reloads the current page.

```python
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.example.com")

print("Before refresh:", driver.title)

driver.refresh()

print("After refresh:", driver.title)  # Same title, page reloaded
```

**Use case:** Useful when testing live-updating content, cache busting, or form reset behavior.

---

## Element Content & Attributes

### `text`

A property that returns the **visible inner text** of an element, stripping all HTML tags. Returns an empty string if the element has no visible text.

```python
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.example.com")

# HTML: <h1 class="heading">Welcome to Example</h1>
heading = driver.find_element(By.TAG_NAME, "h1")
print(heading.text)
# Output: Welcome to Example

# HTML: <p>This is a <strong>bold</strong> paragraph.</p>
paragraph = driver.find_element(By.TAG_NAME, "p")
print(paragraph.text)
# Output: This is a bold paragraph.

# Iterating over multiple elements
items = driver.find_elements(By.CSS_SELECTOR, "ul.menu li")
for item in items:
    print(item.text)
```

> 📝 `text` returns only **visible** text. Hidden elements (`display: none`) return an empty string.

---

### `get_attribute()`

Returns the value of a **specified HTML attribute** of an element. Returns `None` if the attribute does not exist.

**Syntax:**

```python
element.get_attribute("attribute_name")
```

```python
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.example.com")

# --- href attribute ---
# HTML: <a href="https://www.docs.example.com" target="_blank">Docs</a>
link = driver.find_element(By.TAG_NAME, "a")
print(link.get_attribute("href"))     # https://www.docs.example.com
print(link.get_attribute("target"))   # _blank

# --- Input value ---
# HTML: <input type="text" id="username" value="john_doe" placeholder="Enter name">
username_field = driver.find_element(By.ID, "username")
print(username_field.get_attribute("value"))        # john_doe
print(username_field.get_attribute("placeholder"))  # Enter name
print(username_field.get_attribute("type"))         # text

# --- Image src ---
# HTML: <img id="logo" src="/images/logo.png" alt="Company Logo">
img = driver.find_element(By.ID, "logo")
print(img.get_attribute("src"))   # https://www.example.com/images/logo.png
print(img.get_attribute("alt"))   # Company Logo

# --- Boolean attributes ---
# HTML: <input type="checkbox" id="agree" checked>
checkbox = driver.find_element(By.ID, "agree")
print(checkbox.get_attribute("checked"))   # "true"

# --- Class and ID ---
# HTML: <div class="container main-wrapper" id="app">
div = driver.find_element(By.ID, "app")
print(div.get_attribute("class"))  # container main-wrapper
print(div.get_attribute("id"))     # app
```

**`text` vs `get_attribute("innerHTML")` vs `get_attribute("textContent")`:**

| Method                          | Returns                                     |
| ------------------------------- | ------------------------------------------- |
| `.text`                         | Visible text only (respects CSS visibility) |
| `.get_attribute("textContent")` | All text including hidden text              |
| `.get_attribute("innerHTML")`   | Raw HTML including child tags               |
| `.get_attribute("outerHTML")`   | Full HTML including the element's own tag   |

```python
# HTML: <div id="box" style="display:none">Secret</div>
box = driver.find_element(By.ID, "box")

print(box.text)                             # ""  (hidden, not visible)
print(box.get_attribute("textContent"))     # "Secret"
print(box.get_attribute("innerHTML"))       # "Secret"
print(box.get_attribute("outerHTML"))       # '<div id="box" ...>Secret</div>'
```

---

## Full Example Script

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# --- Setup ---
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    # Navigate to a page
    driver.get("https://en.wikipedia.org/wiki/Python_(programming_language)")

    # --- Basic Attributes ---
    print("Title:", driver.title)
    print("URL:", driver.current_url)
    print("Page source length:", len(driver.page_source), "chars")

    # --- Find Elements ---
    heading = driver.find_element(By.TAG_NAME, "h1")
    print("\nMain heading text:", heading.text)

    all_links = driver.find_elements(By.TAG_NAME, "a")
    print(f"Total links on page: {len(all_links)}")

    # --- get_attribute() ---
    first_link = driver.find_element(By.CSS_SELECTOR, "#content a")
    print("\nFirst link href:", first_link.get_attribute("href"))
    print("First link text:", first_link.text)

    # --- is_displayed() ---
    print("\nHeading displayed:", heading.is_displayed())
    print("Heading enabled:", heading.is_enabled())

    # --- Navigation ---
    driver.get("https://www.python.org")
    print("\nNavigated to:", driver.title)

    driver.back()
    print("After back():", driver.title)

    driver.forward()
    print("After forward():", driver.title)

    driver.refresh()
    print("After refresh():", driver.title)

    time.sleep(1)

finally:
    # --- Always quit to clean up ---
    driver.quit()
    print("\nBrowser closed successfully.")
```

---

## Quick Reference Cheat Sheet

| Feature              | Syntax                                | Returns            |
| -------------------- | ------------------------------------- | ------------------ |
| Page title           | `driver.title`                        | `str`              |
| Current URL          | `driver.current_url`                  | `str`              |
| HTML source          | `driver.page_source`                  | `str`              |
| Close current tab    | `driver.close()`                      | `None`             |
| Close all + session  | `driver.quit()`                       | `None`             |
| Find one element     | `driver.find_element(By.X, "value")`  | `WebElement`       |
| Find all elements    | `driver.find_elements(By.X, "value")` | `List[WebElement]` |
| Is visible?          | `element.is_displayed()`              | `bool`             |
| Is interactive?      | `element.is_enabled()`                | `bool`             |
| Is checked/selected? | `element.is_selected()`               | `bool`             |
| Go back              | `driver.back()`                       | `None`             |
| Go forward           | `driver.forward()`                    | `None`             |
| Reload page          | `driver.refresh()`                    | `None`             |
| Visible text         | `element.text`                        | `str`              |
| HTML attribute value | `element.get_attribute("attr_name")`  | `str` or `None`    |
