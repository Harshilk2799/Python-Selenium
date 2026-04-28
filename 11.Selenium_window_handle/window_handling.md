# Python Selenium Window Handling

## Introduction

Window handling in Selenium refers to managing multiple browser windows or tabs during automated testing or web scraping. When a web application opens new windows or tabs, Selenium provides tools to switch between them, retrieve their handles, and manage them effectively.

---

## Core Concepts

### Window Handle

A **window handle** is a unique identifier (string) assigned to each browser window or tab. Selenium uses these handles to switch between open windows.

```python
# Get the current window handle
current_handle = driver.current_window_handle

# Get all open window handles
all_handles = driver.window_handles
```

---

## Setup

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.implicitly_wait(10)
```

---

## Example 1: Switching to a New Window/Tab

When a link opens a new tab or window, you must switch to it using its handle.

```python
driver.get("https://example.com")

# Store the original window handle
original_window = driver.current_window_handle

# Click a link that opens a new window/tab
driver.find_element(By.LINK_TEXT, "Open New Tab").click()

# Wait until a new window is opened
WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))

# Loop through all handles and switch to the new one
for handle in driver.window_handles:
    if handle != original_window:
        driver.switch_to.window(handle)
        break

print("New Window Title:", driver.title)
print("New Window URL:", driver.current_url)
```

---

## Example 2: Switching Back to the Original Window

After working in a new window, you can switch back to the original window using its stored handle.

```python
# Switch back to the original window
driver.switch_to.window(original_window)

print("Back to Original Window:", driver.title)
```

---

## Example 3: Handling Multiple Windows

When multiple windows are opened, iterate over all handles to manage them.

```python
driver.get("https://example.com")

original_window = driver.current_window_handle

# Simulate opening multiple new windows
driver.find_element(By.ID, "open-window-1").click()
driver.find_element(By.ID, "open-window-2").click()

# Wait for all windows to open
WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(3))

all_windows = driver.window_handles
print(f"Total Windows Open: {len(all_windows)}")

# Iterate and process each window
for handle in all_windows:
    driver.switch_to.window(handle)
    print(f"Window Handle: {handle} | Title: {driver.title}")

# Switch back to original
driver.switch_to.window(original_window)
```

---

## Example 4: Opening a New Tab Programmatically

You can open a new tab using JavaScript execution.

```python
driver.get("https://example.com")

# Open a new tab using JavaScript
driver.execute_script("window.open('https://google.com', '_blank');")

# Wait for the new tab to open
WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))

# Switch to the new tab
new_tab = [h for h in driver.window_handles if h != driver.current_window_handle][0]
driver.switch_to.window(new_tab)

print("New Tab Title:", driver.title)
```

---

## Example 5: Closing a Specific Window

You can close a specific window and switch back to another one.

```python
driver.get("https://example.com")
original_window = driver.current_window_handle

# Open a new window
driver.execute_script("window.open('https://python.org', '_blank');")
WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))

# Switch to new window
for handle in driver.window_handles:
    if handle != original_window:
        driver.switch_to.window(handle)
        break

print("On New Window:", driver.title)

# Close the new window
driver.close()

# Switch back to original
driver.switch_to.window(original_window)
print("Back to Original:", driver.title)
```

---

## Example 6: Full Workflow — Multi-Window Automation

A complete example that opens multiple windows, processes each one, and cleans up.

```python
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def handle_multiple_windows():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    try:
        driver.get("https://example.com")
        original_window = driver.current_window_handle

        # Open two new tabs
        driver.execute_script("window.open('https://python.org', '_blank');")
        driver.execute_script("window.open('https://selenium.dev', '_blank');")

        wait.until(EC.number_of_windows_to_be(3))

        all_handles = driver.window_handles
        print(f"Total windows: {len(all_handles)}\n")

        # Process each window
        for i, handle in enumerate(all_handles):
            driver.switch_to.window(handle)
            print(f"Window {i + 1}: {driver.title} | URL: {driver.current_url}")

        # Close all except original
        for handle in all_handles:
            if handle != original_window:
                driver.switch_to.window(handle)
                driver.close()

        # Return to original
        driver.switch_to.window(original_window)
        print(f"\nBack to original: {driver.title}")

    finally:
        driver.quit()

handle_multiple_windows()
```

---

## Key Methods Summary

| Method                                      | Description                                       |
| ------------------------------------------- | ------------------------------------------------- |
| `driver.current_window_handle`              | Returns the handle of the currently active window |
| `driver.window_handles`                     | Returns a list of all open window handles         |
| `driver.switch_to.window(handle)`           | Switches focus to the specified window handle     |
| `driver.close()`                            | Closes the currently focused window               |
| `driver.quit()`                             | Closes all windows and ends the WebDriver session |
| `driver.execute_script("window.open(...)")` | Opens a new tab/window programmatically via JS    |

---

## Best Practices

1. **Always store the original window handle** before performing any actions that open new windows.
2. **Use `WebDriverWait`** to wait for new windows to appear instead of using `time.sleep()`.
3. **Always switch back** to the intended window after your task is done in a new window.
4. **Use `driver.quit()`** at the end of your script to close all windows and free up resources.
5. **Handle exceptions** (e.g., `NoSuchWindowException`) when switching between windows to make scripts robust.

---

## Common Exception

```python
from selenium.common.exceptions import NoSuchWindowException

try:
    driver.switch_to.window("invalid_handle")
except NoSuchWindowException:
    print("Window no longer exists or handle is invalid.")
```

---

## Conclusion

Selenium window handling is essential for testing and automating web applications that open multiple tabs or windows. By mastering `current_window_handle`, `window_handles`, and `switch_to.window()`, you can effectively navigate complex multi-window workflows with confidence.
