# Python Selenium XPATH — Complete Guide

---

## What is XPATH?

**XPath (XML Path Language)** is a query language used to navigate and select nodes in an XML or HTML document. In Selenium, XPath is one of the most powerful and flexible locator strategies to find web elements — especially when elements lack unique `id` or `name` attributes.

---

## XPath Syntax Basics

```
//tagname[@attribute='value']
```

| Symbol | Meaning                                |
| ------ | -------------------------------------- |
| `/`    | Selects from the root node             |
| `//`   | Selects nodes anywhere in the document |
| `.`    | Selects the current node               |
| `..`   | Selects the parent of the current node |
| `@`    | Selects an attribute                   |
| `*`    | Wildcard — matches any element         |
| `[]`   | Predicate — filters nodes              |

---

## Types of XPath

### 1. Absolute XPath

Starts from the root of the HTML document. Fragile — breaks if structure changes.

```python
driver.find_element("xpath", "/html/body/div[1]/form/input[1]")
```

### 2. Relative XPath ✅ (Recommended)

Starts from anywhere in the document using `//`. More robust and maintainable.

```python
driver.find_element("xpath", "//input[@id='username']")
```

---

## Core XPath Examples

### 1. Locate by `id`

```python
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://example.com/login")

# Find input field with id="username"
username = driver.find_element("xpath", "//input[@id='username']")
username.send_keys("john_doe")
```

---

### 2. Locate by `name`

```python
# Find input with name="password"
password = driver.find_element("xpath", "//input[@name='password']")
password.send_keys("secret123")
```

---

### 3. Locate by `class`

```python
# Find a button with class="submit-btn"
submit = driver.find_element("xpath", "//button[@class='submit-btn']")
submit.click()
```

---

### 4. Locate by `text()` — Exact Match

```python
# Find a link whose visible text is exactly "Sign In"
sign_in = driver.find_element("xpath", "//a[text()='Sign In']")
sign_in.click()
```

---

### 5. Locate using `contains()` — Partial Match

```python
# Useful when class names or text can be dynamic/partial
element = driver.find_element("xpath", "//button[contains(text(),'Submit')]")
element.click()

# Partial class name match
card = driver.find_element("xpath", "//div[contains(@class,'product-card')]")
```

---

### 6. Locate using `starts-with()`

```python
# Match elements whose attribute value starts with a given string
element = driver.find_element("xpath", "//input[starts-with(@id,'user')]")
```

---

### 7. Using `and` / `or` Operators

```python
# AND — both conditions must be true
element = driver.find_element("xpath", "//input[@type='text' and @name='email']")

# OR — at least one condition must be true
element = driver.find_element("xpath", "//input[@id='phone' or @name='phone']")
```

---

### 8. Parent, Child, and Sibling Axes

```python
# Select parent of an element
parent = driver.find_element("xpath", "//input[@id='email']/..")

# Select direct child
child = driver.find_element("xpath", "//ul[@id='menu']/li")

# Select all descendants
desc = driver.find_elements("xpath", "//div[@id='container']//span")

# Following sibling
sibling = driver.find_element("xpath", "//label[text()='Username']/following-sibling::input")

# Preceding sibling
prev = driver.find_element("xpath", "//input[@id='email']/preceding-sibling::label")
```

---

### 9. XPath with Index (Position)

```python
# Select the 2nd <li> element inside a <ul>
second_item = driver.find_element("xpath", "//ul[@id='nav']/li[2]")

# Select last element
last_item = driver.find_element("xpath", "//ul[@id='nav']/li[last()]")

# Select second-to-last
second_last = driver.find_element("xpath", "//ul[@id='nav']/li[last()-1]")
```

---

### 10. `find_elements` — Multiple Elements

```python
# Returns a list of all matching elements
rows = driver.find_elements("xpath", "//table[@id='data-table']//tr")

for row in rows:
    print(row.text)
```

---

### 11. Wildcard `*` — Any Tag

```python
# Match any element with a given attribute
element = driver.find_element("xpath", "//*[@placeholder='Search...']")

# Any child of a div
children = driver.find_elements("xpath", "//div[@id='wrapper']/*")
```

---

### 12. Nested / Chained Conditions

```python
# Find a <td> inside a <tr> where another <td> has specific text
cell = driver.find_element(
    "xpath",
    "//tr[td[text()='Alice']]/td[2]"
)
print(cell.text)  # prints the value in the 2nd column of Alice's row
```

---

### 13. XPath with `normalize-space()` — Handle Whitespace

```python
# Handles extra spaces in element text
element = driver.find_element(
    "xpath",
    "//button[normalize-space(text())='Click Me']"
)
```

---

### 14. Real-World: Login Form Automation

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://example.com/login")

wait = WebDriverWait(driver, 10)

# Wait and locate using XPath
username = wait.until(EC.presence_of_element_located(("xpath", "//input[@id='username']")))
username.send_keys("admin")

password = driver.find_element("xpath", "//input[@type='password']")
password.send_keys("admin123")

login_btn = driver.find_element("xpath", "//button[contains(text(),'Login')]")
login_btn.click()

# Verify login success
dashboard = wait.until(EC.presence_of_element_located(("xpath", "//h1[text()='Dashboard']")))
print("Login successful:", dashboard.text)

driver.quit()
```

---

### 15. Real-World: Scraping a Table

```python
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://example.com/data-table")

rows = driver.find_elements("xpath", "//table[@id='results']//tbody/tr")

for row in rows:
    cols = row.find_elements("xpath", ".//td")  # relative xpath from row
    data = [col.text for col in cols]
    print(data)

driver.quit()
```

---

## XPath Axes — Quick Reference

| Axis                | Description      | Example                            |
| ------------------- | ---------------- | ---------------------------------- |
| `child`             | Direct children  | `//div/child::span`                |
| `parent`            | Parent node      | `//input/parent::form`             |
| `ancestor`          | All ancestors    | `//span/ancestor::div`             |
| `descendant`        | All descendants  | `//div/descendant::input`          |
| `following-sibling` | Siblings after   | `//label/following-sibling::input` |
| `preceding-sibling` | Siblings before  | `//input/preceding-sibling::label` |
| `following`         | All nodes after  | `//h1/following::p`                |
| `preceding`         | All nodes before | `//footer/preceding::nav`          |

---

## XPath Functions — Quick Reference

| Function            | Use Case           | Example                             |
| ------------------- | ------------------ | ----------------------------------- |
| `text()`            | Match visible text | `//p[text()='Hello']`               |
| `contains()`        | Partial match      | `//div[contains(@class,'btn')]`     |
| `starts-with()`     | Prefix match       | `//input[starts-with(@name,'usr')]` |
| `normalize-space()` | Trim whitespace    | `//span[normalize-space()='OK']`    |
| `not()`             | Negate condition   | `//input[not(@disabled)]`           |
| `count()`           | Count nodes        | `count(//li)`                       |
| `last()`            | Last element index | `//li[last()]`                      |
| `position()`        | Position in list   | `//li[position()=3]`                |

---

## Common Mistakes & Tips

| ❌ Mistake                                 | ✅ Fix                                        |
| ------------------------------------------ | --------------------------------------------- |
| Using absolute XPath                       | Use relative XPath with `//`                  |
| Hardcoding dynamic IDs                     | Use `contains()` or `starts-with()`           |
| Not waiting for elements                   | Use `WebDriverWait` with `ExpectedConditions` |
| Case-sensitive text mismatch               | Use `normalize-space()` or `translate()`      |
| Using `find_element` for multiple elements | Use `find_elements` and iterate               |

---

## Summary

- **XPath** is a powerful locator for Selenium when CSS selectors aren't sufficient.
- Prefer **relative XPath** (`//`) over absolute paths.
- Use `contains()`, `starts-with()`, `text()` for flexible matching.
- Use **axes** (`parent`, `following-sibling`, etc.) to navigate the DOM tree.
- Always combine with **explicit waits** (`WebDriverWait`) in real automation.

---

_Guide covers Python Selenium with XPath — suitable for beginners to intermediate automation engineers._
