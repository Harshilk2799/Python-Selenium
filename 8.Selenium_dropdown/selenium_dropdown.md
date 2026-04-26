# Dropdown & Multi-Select Handling in Selenium

## Dropdown Handling in Selenium

### Overview

To interact with dropdown elements in Selenium:

- Identify the dropdown element
- Wrap it using the `Select` class from `selenium.webdriver.support.select`

---

### Ways to Select Options

There are **3 built-in methods** to select values from a dropdown:

#### 1. select_by_index

- Select option using its index (starts from 0)

#### 2. select_by_value

- Select option using the `value` attribute

#### 3. select_by_visible_text

- Select option using the visible text

---

### Access All Dropdown Options

- Use `.options` attribute to fetch all options
- You can count total options and print their visible text

---

### Select Option Without Built-in Methods

- Iterate through all options
- Compare text with desired value
- Click the matching option

---

### Key Points

- Always wrap `<select>` elements using `Select`
- Prefer `select_by_visible_text` for readability
- Use `.options` to inspect dropdown contents
- Manual iteration is useful when custom logic is needed

---

## Multi-Select Dropdown Handling in Selenium

### Overview

- Multi-select dropdowns allow selecting **multiple options simultaneously**
- Handled using the same `Select` class as single dropdowns

---

### Select Methods

There are multiple ways to select options:

#### 1. select_by_index

- Select option using its index (starts from 0)

#### 2. select_by_value

- Select option using the `value` attribute

#### 3. select_by_visible_text

- Select option using the visible text

---

### Deselect Methods

There are multiple ways to deselect options:

#### 1. deselect_by_index

- Deselect option using its index

#### 2. deselect_by_value

- Deselect option using the `value` attribute

#### 3. deselect_by_visible_text

- Deselect option using the visible text

#### 4. deselect_all

- Deselect all selected options
- Does not require any arguments

---

### Key Points

- Multi-select dropdown must support multiple selection (`multiple` attribute present)
- Same `Select` class is used for handling
- You can select and deselect options dynamically
- Use `deselect_all` to clear all selections at once
