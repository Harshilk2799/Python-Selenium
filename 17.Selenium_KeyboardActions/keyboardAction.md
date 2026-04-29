# Python Selenium – Keyboard Actions

A complete guide to simulating keyboard input using Selenium WebDriver in Python.

---

## Table of Contents

1. [Introduction](#introduction)
2. [Setup & Prerequisites](#setup--prerequisites)
3. [Sending Keys with `send_keys()`](#1-sending-keys-with-send_keys)
4. [Special Keys with `Keys` Class](#2-special-keys-with-keys-class)
5. [Key Combinations (Shortcuts)](#3-key-combinations-shortcuts)
6. [ActionChains for Keyboard Actions](#4-actionchains-for-keyboard-actions)
7. [key_down() and key_up()](#5-key_down-and-key_up)
8. [Clearing Input Fields](#6-clearing-input-fields)
9. [Typing with Delay (Human-like)](#7-typing-with-delay-human-like)
10. [Keyboard Actions on Non-Input Elements](#8-keyboard-actions-on-non-input-elements)
11. [Common Use Cases](#9-common-use-cases)
12. [Best Practices](#10-best-practices)
13. [Quick Reference Table](#quick-reference-table)

---

## Introduction

Selenium WebDriver allows you to simulate real keyboard interactions on web pages. This is essential for:

- Filling out forms
- Triggering keyboard shortcuts
- Navigating through UI elements using Tab, Enter, Arrow keys
- Testing accessibility features

Keyboard actions in Selenium are primarily handled through:

- `element.send_keys()` — type text or press keys on an element
- `Keys` class — constants for special keys (Enter, Tab, Ctrl, etc.)
- `ActionChains` — chain complex keyboard sequences

---

## Setup & Prerequisites

### Installation

```bash
pip install selenium
```

### Basic Imports

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
```

### Starting the Browser

```python
driver = webdriver.Chrome()
driver.get("https://example.com")
```

---

## 1. Sending Keys with `send_keys()`

The simplest way to type into an input field.

### Syntax

```python
element.send_keys("your text here")
```

### Example – Typing into a Search Box

```python
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.google.com")

search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Python Selenium tutorial")

driver.quit()
```

### Example – Filling a Login Form

```python
driver.get("https://example.com/login")

username = driver.find_element(By.ID, "username")
password = driver.find_element(By.ID, "password")

username.send_keys("myuser@email.com")
password.send_keys("SecurePassword123")
```

---

## 2. Special Keys with `Keys` Class

The `Keys` class provides constants for non-printable keys.

### Common Special Keys

| Key Constant           | Description        |
| ---------------------- | ------------------ |
| `Keys.ENTER`           | Enter / Return key |
| `Keys.TAB`             | Tab key            |
| `Keys.SPACE`           | Spacebar           |
| `Keys.BACKSPACE`       | Backspace key      |
| `Keys.DELETE`          | Delete key         |
| `Keys.ESCAPE`          | Escape key         |
| `Keys.ARROW_UP`        | Up arrow key       |
| `Keys.ARROW_DOWN`      | Down arrow key     |
| `Keys.ARROW_LEFT`      | Left arrow key     |
| `Keys.ARROW_RIGHT`     | Right arrow key    |
| `Keys.HOME`            | Home key           |
| `Keys.END`             | End key            |
| `Keys.PAGE_UP`         | Page Up            |
| `Keys.PAGE_DOWN`       | Page Down          |
| `Keys.F1` – `Keys.F12` | Function keys      |
| `Keys.CONTROL`         | Ctrl key           |
| `Keys.ALT`             | Alt key            |
| `Keys.SHIFT`           | Shift key          |

### Example – Press Enter After Typing

```python
from selenium.webdriver.common.keys import Keys

search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Selenium Python")
search_box.send_keys(Keys.ENTER)   # Submit the search
```

### Example – Navigate with Tab Key

```python
first_field = driver.find_element(By.ID, "first_name")
first_field.send_keys("John")
first_field.send_keys(Keys.TAB)   # Move to next field

# Now the next input field is focused
second_field = driver.switch_to.active_element
second_field.send_keys("Doe")
```

### Example – Use Arrow Keys in a Dropdown

```python
dropdown = driver.find_element(By.ID, "country-select")
dropdown.click()
dropdown.send_keys(Keys.ARROW_DOWN)  # Move down one option
dropdown.send_keys(Keys.ARROW_DOWN)  # Move down again
dropdown.send_keys(Keys.ENTER)       # Select the option
```

---

## 3. Key Combinations (Shortcuts)

You can combine multiple keys in a single `send_keys()` call to trigger keyboard shortcuts.

### Example – Select All Text (Ctrl+A)

```python
input_field = driver.find_element(By.ID, "text-input")
input_field.send_keys(Keys.CONTROL + "a")   # Ctrl+A: Select All
```

### Example – Copy and Paste (Ctrl+C / Ctrl+V)

```python
input_field = driver.find_element(By.ID, "source")
input_field.send_keys(Keys.CONTROL + "a")   # Select all
input_field.send_keys(Keys.CONTROL + "c")   # Copy

target_field = driver.find_element(By.ID, "target")
target_field.send_keys(Keys.CONTROL + "v")  # Paste
```

### Example – Undo and Redo (Ctrl+Z / Ctrl+Y)

```python
editor = driver.find_element(By.ID, "editor")
editor.send_keys("Hello World")
editor.send_keys(Keys.CONTROL + "z")   # Undo last action
editor.send_keys(Keys.CONTROL + "y")   # Redo
```

### Example – Select All and Replace

```python
field = driver.find_element(By.ID, "bio")
field.send_keys(Keys.CONTROL + "a")    # Select existing text
field.send_keys("New replacement text")  # Replace with new text
```

> **macOS Note:** Replace `Keys.CONTROL` with `Keys.COMMAND` for Mac shortcuts.

---

## 4. ActionChains for Keyboard Actions

`ActionChains` lets you build complex, multi-step keyboard (and mouse) sequences that are executed together.

### Syntax

```python
actions = ActionChains(driver)
actions.some_action().another_action().perform()
```

### Example – Type Text Using ActionChains

```python
from selenium.webdriver.common.action_chains import ActionChains

element = driver.find_element(By.ID, "message")
actions = ActionChains(driver)
actions.click(element)
actions.send_keys("Hello from ActionChains!")
actions.perform()
```

### Example – Press Multiple Keys in Sequence

```python
actions = ActionChains(driver)
actions.send_keys("Line one")
actions.send_keys(Keys.SHIFT + Keys.ENTER)   # Shift+Enter: new line (in some editors)
actions.send_keys("Line two")
actions.perform()
```

### Example – Navigate a Rich Text Editor

```python
editor = driver.find_element(By.CLASS_NAME, "ql-editor")   # e.g., Quill editor

actions = ActionChains(driver)
actions.click(editor)
actions.send_keys("This is ")
actions.key_down(Keys.CONTROL)
actions.send_keys("b")             # Ctrl+B: Bold On
actions.key_up(Keys.CONTROL)
actions.send_keys("bold text")
actions.key_down(Keys.CONTROL)
actions.send_keys("b")             # Ctrl+B: Bold Off
actions.key_up(Keys.CONTROL)
actions.perform()
```

---

## 5. `key_down()` and `key_up()`

These methods explicitly press and release modifier keys (Ctrl, Shift, Alt), giving you full control over key state.

### Syntax

```python
actions.key_down(Keys.CONTROL)   # Hold Ctrl
actions.send_keys("c")           # Press C while Ctrl is held
actions.key_up(Keys.CONTROL)     # Release Ctrl
actions.perform()
```

### Example – Shift+Click to Select Multiple Items

```python
items = driver.find_elements(By.CSS_SELECTOR, ".list-item")

actions = ActionChains(driver)
actions.click(items[0])              # Click first item
actions.key_down(Keys.SHIFT)
actions.click(items[3])              # Shift+Click fourth item (selects range)
actions.key_up(Keys.SHIFT)
actions.perform()
```

### Example – Ctrl+Click to Select Non-Contiguous Items

```python
checkboxes = driver.find_elements(By.CSS_SELECTOR, ".checkbox")

actions = ActionChains(driver)
actions.click(checkboxes[0])
actions.key_down(Keys.CONTROL)
actions.click(checkboxes[2])         # Ctrl+Click: add to selection
actions.click(checkboxes[4])         # Ctrl+Click another
actions.key_up(Keys.CONTROL)
actions.perform()
```

### Example – Typing in ALL CAPS with Shift Held

```python
element = driver.find_element(By.ID, "heading")
actions = ActionChains(driver)
actions.click(element)
actions.key_down(Keys.SHIFT)
actions.send_keys("important message")   # Types: IMPORTANT MESSAGE
actions.key_up(Keys.SHIFT)
actions.perform()
```

---

## 6. Clearing Input Fields

Before typing new content, it's often necessary to clear the existing value.

### Method 1: `clear()` built-in

```python
field = driver.find_element(By.ID, "email")
field.clear()                             # Removes all text
field.send_keys("newemail@example.com")
```

### Method 2: Select All + Delete

Useful when `clear()` doesn't work (e.g., React/Angular-controlled inputs):

```python
field = driver.find_element(By.ID, "search")
field.send_keys(Keys.CONTROL + "a")    # Select all
field.send_keys(Keys.DELETE)           # Delete selection
field.send_keys("New search query")
```

### Method 3: Using ActionChains

```python
field = driver.find_element(By.ID, "notes")
actions = ActionChains(driver)
actions.triple_click(field)            # Triple-click to select all
actions.send_keys("Fresh content")     # Replaces selected text
actions.perform()
```

---

## 7. Typing with Delay (Human-like)

Real users don't type instantly. Adding delays makes automation less detectable and more realistic.

### Example – Character-by-Character Typing

```python
import time

def slow_type(element, text, delay=0.1):
    """Type text one character at a time with a delay."""
    for char in text:
        element.send_keys(char)
        time.sleep(delay)

field = driver.find_element(By.ID, "message")
slow_type(field, "Hello, I am typing slowly!", delay=0.15)
```

### Example – Typing with Random Delay (More Human-like)

```python
import time
import random

def human_type(element, text):
    """Type with a random delay between characters."""
    for char in text:
        element.send_keys(char)
        time.sleep(random.uniform(0.05, 0.25))   # 50ms to 250ms

search = driver.find_element(By.NAME, "q")
human_type(search, "Python automation")
```

---

## 8. Keyboard Actions on Non-Input Elements

Some keyboard actions apply to the whole page or to non-input elements like `<div>`, `<body>`, etc.

### Example – Scroll Page with Arrow/Page Keys

```python
from selenium.webdriver.common.by import By

# Focus the body element and use keyboard to scroll
body = driver.find_element(By.TAG_NAME, "body")
body.send_keys(Keys.PAGE_DOWN)   # Scroll down one page
body.send_keys(Keys.PAGE_DOWN)
body.send_keys(Keys.PAGE_UP)     # Scroll back up
```

### Example – Dismiss a Modal with Escape

```python
# A modal or popup is open; press Escape to close it
actions = ActionChains(driver)
actions.send_keys(Keys.ESCAPE)
actions.perform()
```

### Example – Navigate a Menu with Arrow Keys

```python
menu_button = driver.find_element(By.ID, "nav-menu")
menu_button.click()                              # Open menu

actions = ActionChains(driver)
actions.send_keys(Keys.ARROW_DOWN)              # Focus first item
actions.send_keys(Keys.ARROW_DOWN)              # Move to second item
actions.send_keys(Keys.ENTER)                   # Select item
actions.perform()
```

---

## 9. Common Use Cases

### Use Case 1 – Complete Login Flow

```python
driver.get("https://example.com/login")

email = driver.find_element(By.ID, "email")
email.send_keys("user@example.com")
email.send_keys(Keys.TAB)                       # Move to password field

password = driver.switch_to.active_element
password.send_keys("mypassword")
password.send_keys(Keys.ENTER)                  # Submit the form
```

### Use Case 2 – Fill and Submit a Registration Form

```python
driver.get("https://example.com/register")

fields = {
    "first_name": "Alice",
    "last_name": "Smith",
    "email": "alice@example.com",
    "password": "P@ssword123",
}

for field_id, value in fields.items():
    field = driver.find_element(By.ID, field_id)
    field.clear()
    field.send_keys(value)

# Submit with Enter key
driver.find_element(By.ID, "password").send_keys(Keys.ENTER)
```

### Use Case 3 – Search Autocomplete Navigation

```python
search = driver.find_element(By.ID, "search-input")
search.send_keys("Pyt")                         # Trigger autocomplete

time.sleep(1)                                   # Wait for suggestions

search.send_keys(Keys.ARROW_DOWN)               # Move to first suggestion
search.send_keys(Keys.ARROW_DOWN)               # Move to second suggestion
search.send_keys(Keys.ENTER)                    # Select it
```

### Use Case 4 – Select a Date in a Date Picker

```python
date_input = driver.find_element(By.ID, "date")
date_input.click()

# Navigate calendar using arrow keys
actions = ActionChains(driver)
actions.send_keys(Keys.ARROW_RIGHT)             # Next day
actions.send_keys(Keys.ARROW_RIGHT)
actions.send_keys(Keys.ENTER)
actions.perform()
```

---

## 10. Best Practices

- **Always wait for elements** before interacting — use `WebDriverWait` to avoid `NoSuchElementException`.
- **Use `clear()` before `send_keys()`** to avoid appending to existing field values.
- **Prefer `Keys` constants** over hardcoded Unicode characters for special keys.
- **Release modifier keys** — always pair `key_down()` with `key_up()` to avoid keys staying "stuck".
- **Use ActionChains for complex sequences** — chaining ensures the browser processes inputs in order.
- **Add small delays** when filling multiple fields in quick succession for stability.
- **Check element focus** — some keyboard events only fire when the element is focused.

---

## Quick Reference Table

| Task                   | Code                                            |
| ---------------------- | ----------------------------------------------- |
| Type text              | `element.send_keys("text")`                     |
| Press Enter            | `element.send_keys(Keys.ENTER)`                 |
| Press Tab              | `element.send_keys(Keys.TAB)`                   |
| Press Backspace        | `element.send_keys(Keys.BACKSPACE)`             |
| Select All             | `element.send_keys(Keys.CONTROL + "a")`         |
| Copy                   | `element.send_keys(Keys.CONTROL + "c")`         |
| Paste                  | `element.send_keys(Keys.CONTROL + "v")`         |
| Undo                   | `element.send_keys(Keys.CONTROL + "z")`         |
| Clear field            | `element.clear()`                               |
| Hold Ctrl              | `actions.key_down(Keys.CONTROL)`                |
| Release Ctrl           | `actions.key_up(Keys.CONTROL)`                  |
| Arrow navigation       | `element.send_keys(Keys.ARROW_DOWN)`            |
| Scroll page            | `body.send_keys(Keys.PAGE_DOWN)`                |
| Dismiss modal          | `actions.send_keys(Keys.ESCAPE).perform()`      |
| Chain keyboard actions | `ActionChains(driver).send_keys(...).perform()` |

---

_Generated for Python Selenium — compatible with Selenium 4.x_
