# Python Selenium Action Chains

## What is ActionChains?

`ActionChains` is a class in Selenium WebDriver that allows you to automate **low-level interactions** such as mouse movements, mouse button actions, key presses, and context menu interactions. It is ideal for simulating complex user gestures that go beyond simple `.click()` or `.send_keys()` calls.

ActionChains follow a **queue-based model**: actions are chained together and only executed when `.perform()` is called.

---

## Import & Setup

```python
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://example.com")

actions = ActionChains(driver)
```

---

## Core Concepts

| Method                     | Description                              |
| -------------------------- | ---------------------------------------- |
| `click(element)`           | Left-click on an element                 |
| `double_click(element)`    | Double-click on an element               |
| `context_click(element)`   | Right-click (context menu) on an element |
| `click_and_hold(element)`  | Press and hold the left mouse button     |
| `release(element)`         | Release the held mouse button            |
| `move_to_element(element)` | Hover over an element                    |
| `move_by_offset(x, y)`     | Move mouse by pixel offset               |
| `drag_and_drop(src, tgt)`  | Drag element from source to target       |
| `send_keys(*keys)`         | Send keyboard keys                       |
| `key_down(key)`            | Press and hold a modifier key            |
| `key_up(key)`              | Release a modifier key                   |
| `pause(seconds)`           | Pause the chain for given seconds        |
| `perform()`                | Execute all queued actions               |
| `reset_actions()`          | Clear all queued actions                 |

---

## Examples

### 1. Hover Over an Element (Mouse Over)

Hovering is used to trigger dropdown menus or tooltips.

```python
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://example.com")

menu = driver.find_element(By.ID, "nav-menu")

actions = ActionChains(driver)
actions.move_to_element(menu).perform()

# Now interact with the revealed dropdown item
submenu = driver.find_element(By.ID, "submenu-item")
submenu.click()
```

---

### 2. Double Click

```python
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://example.com")

element = driver.find_element(By.ID, "double-click-btn")

actions = ActionChains(driver)
actions.double_click(element).perform()
```

---

### 3. Right Click (Context Menu)

```python
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://example.com")

element = driver.find_element(By.ID, "right-click-area")

actions = ActionChains(driver)
actions.context_click(element).perform()

# Now select an option from the context menu
menu_option = driver.find_element(By.XPATH, "//li[text()='Copy']")
menu_option.click()
```

---

### 4. Drag and Drop

```python
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://example.com/drag-drop")

source = driver.find_element(By.ID, "draggable-item")
target = driver.find_element(By.ID, "drop-zone")

actions = ActionChains(driver)
actions.drag_and_drop(source, target).perform()
```

You can also use `click_and_hold` + `release` for more control:

```python
actions.click_and_hold(source)\
       .move_to_element(target)\
       .release(target)\
       .perform()
```

---

### 5. Drag and Drop by Offset

Useful when there is no target element, only pixel coordinates.

```python
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://example.com")

slider = driver.find_element(By.ID, "slider-handle")

actions = ActionChains(driver)
actions.click_and_hold(slider)\
       .move_by_offset(150, 0)\
       .release()\
       .perform()
```

---

### 6. Key Down & Key Up (Keyboard Shortcuts)

Simulate keyboard shortcuts like `Ctrl+A`, `Ctrl+C`, `Ctrl+V`.

```python
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://example.com")

input_field = driver.find_element(By.ID, "text-input")
input_field.click()

actions = ActionChains(driver)

# Select all text and copy
actions.key_down(Keys.CONTROL)\
       .send_keys("a")\
       .key_up(Keys.CONTROL)\
       .perform()

# Paste into another field
output_field = driver.find_element(By.ID, "output-input")
output_field.click()

actions.reset_actions()
actions.key_down(Keys.CONTROL)\
       .send_keys("v")\
       .key_up(Keys.CONTROL)\
       .perform()
```

---

### 7. Chaining Multiple Actions Together

ActionChains shine when you combine multiple gestures in a single fluent chain.

```python
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://example.com")

menu     = driver.find_element(By.ID, "menu")
btn      = driver.find_element(By.ID, "submit-btn")
text_box = driver.find_element(By.ID, "input-field")

actions = ActionChains(driver)
actions.move_to_element(menu)\        # hover over menu
       .click()\                      # click menu
       .pause(1)\                     # wait 1 second
       .move_to_element(text_box)\    # move to text box
       .click()\                      # focus it
       .send_keys("Hello World")\     # type text
       .key_down(Keys.SHIFT)\         # hold Shift
       .send_keys(Keys.ARROW_UP)\     # select upward
       .key_up(Keys.SHIFT)\           # release Shift
       .double_click(btn)\            # double-click submit
       .perform()
```

---

### 8. Move to Element with Offset

Click at a specific position _within_ an element, rather than its center.

```python
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://example.com")

canvas = driver.find_element(By.ID, "drawing-canvas")

actions = ActionChains(driver)
# Click 50px right and 30px down from the element's top-left corner
actions.move_to_element_with_offset(canvas, 50, 30)\
       .click()\
       .perform()
```

---

### 9. Scroll to Element (Selenium 4+)

Selenium 4 introduced native scroll support via ActionChains.

```python
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://example.com/long-page")

footer = driver.find_element(By.ID, "footer")

actions = ActionChains(driver)
actions.scroll_to_element(footer).perform()
```

---

## Best Practices

- **Always call `.perform()`** — actions are only executed after this call.
- **Use `reset_actions()`** between separate action sequences to avoid stacking old actions.
- **Add explicit waits** (`WebDriverWait`) before chaining to ensure elements are ready.
- **Prefer `drag_and_drop`** for simple cases; use `click_and_hold` + `release` for complex ones.
- **Use `pause()`** in chains to allow animations or transitions to complete.
- **Selenium 4** introduced `scroll_to_element` and improved pointer/keyboard action support over the older API.

---

## Common Pitfall: Forgetting `.perform()`

```python
# ❌ Wrong — nothing happens!
actions.click(button)

# ✅ Correct — action is executed
actions.click(button).perform()
```

---

## Summary

ActionChains let you automate rich, human-like browser interactions in Selenium. By queuing up mouse movements, clicks, drags, keyboard shortcuts, and scrolls — and firing them all with a single `.perform()` — you can handle even the most complex UI scenarios with clean, readable code.
