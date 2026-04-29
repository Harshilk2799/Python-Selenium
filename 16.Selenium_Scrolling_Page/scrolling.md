# Scrolling in Selenium

There are several ways of scrolling a webpage using Selenium:

- Scrolling to a specific element
- Scrolling vertically
- Scrolling horizontally
- Scrolling to the page height
- Infinite scrolling

---

## `execute_script` Method

Scrolling actions are mainly achieved using the **`execute_script`** method.

- Mainly used to execute **JavaScript code** within the context of the currently loaded webpage
- Allows users to directly interact with and manipulate the **Document Object Model (DOM)** of the page
- Helps interact with elements that might not be accessible using Selenium's standard methods
- Better handles **dynamically loaded content** on modern and JavaScript-heavy websites

**Syntax:**

```python
driver.execute_script(script, *args)
```

| Parameter | Description                                                                                |
| --------- | ------------------------------------------------------------------------------------------ |
| `script`  | String containing JavaScript code                                                          |
| `args`    | Optional arguments to pass to the JavaScript code, usually Web Elements or other variables |

---

## 1. Scrolling to a Specific Element

- Identify any element on the webpage
- Use the JavaScript method **`scrollIntoView`**

```python
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://example.com")

# Locate the target element
element = driver.find_element(By.ID, "target-element")

# Scroll the element into view
driver.execute_script("arguments[0].scrollIntoView();", element)
```

---

## 2. Scrolling Vertically

- Use the JavaScript method **`scrollBy`**
- Specify the number of pixels to scroll by
- **Positive value** → scrolls **down**
- **Negative value** → scrolls **up**

```python
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://example.com")

# Scroll down by 500 pixels
driver.execute_script("window.scrollBy(0, 500);")

# Scroll up by 300 pixels
driver.execute_script("window.scrollBy(0, -300);")
```

---

## 3. Scrolling Horizontally

- Similar to scrolling vertically
- The number of pixels is provided as the **first argument**
- **Positive value** → scrolls to the **right**
- **Negative value** → scrolls to the **left**

```python
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://example.com")

# Scroll right by 400 pixels
driver.execute_script("window.scrollBy(400, 0);")

# Scroll left by 200 pixels
driver.execute_script("window.scrollBy(-200, 0);")
```

---

## 4. Scrolling to Page Height

- Use the JavaScript method **`scrollTo`**
- Pass the value `document.body.scrollHeight` in place of pixels
- `document.body.scrollHeight` refers to the **total height of the content** in a webpage

```python
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://example.com")

# Scroll to the bottom of the page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# Scroll back to the top of the page
driver.execute_script("window.scrollTo(0, 0);")
```

---

## 5. Infinite Scrolling

### How It Works

1. Initially, the webpage loads a **fixed amount of content**
2. As the user scrolls close to the bottom, a **JavaScript function triggers** a request to load more content dynamically
3. The new content is added to the page, and the **process repeats**

### Algorithm

1. Get the height of the currently loaded page → `h1`
2. Run an **infinite loop**
3. Scroll down the page to `h1`
4. Inside the loop, get the height of the page again → `h2`
5. If `h1 == h2` → **break** out of the loop (no new content loaded)
6. If `h1 != h2` → update `h1 = h2` and **continue** the loop

### Code

```python
import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://example.com/infinite-scroll")

# Step 1: Get initial page height
h1 = driver.execute_script("return document.body.scrollHeight")

while True:
    # Step 3: Scroll down to current page height
    driver.execute_script("window.scrollTo(0, arguments[0]);", h1)

    # Wait for new content to load
    time.sleep(2)

    # Step 4: Get new page height
    h2 = driver.execute_script("return document.body.scrollHeight")

    # Step 5: Check if new content was loaded
    if h1 == h2:
        print("Reached the end of the page.")
        break  # No new content, exit loop

    # Step 6: Update h1 and continue
    h1 = h2

driver.quit()
```

---

## Summary Table

| Scrolling Type      | JavaScript Method  | Key Parameter                       |
| ------------------- | ------------------ | ----------------------------------- |
| To specific element | `scrollIntoView()` | Web element as argument             |
| Vertically          | `scrollBy(x, y)`   | `y`: `+` down, `-` up               |
| Horizontally        | `scrollBy(x, y)`   | `x`: `+` right, `-` left            |
| To page height      | `scrollTo(x, y)`   | `document.body.scrollHeight`        |
| Infinite scroll     | `scrollTo` + loop  | Compare `scrollHeight` before/after |
