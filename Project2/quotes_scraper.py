from selenium import webdriver 
from selenium.webdriver.common.by import By
import pandas as pd 


driver = webdriver.Chrome()

driver.get("https://quotes.toscrape.com/")
driver.maximize_window()


all_data = []

while True:
    quotes = driver.find_elements(By.CSS_SELECTOR, ".quote")
    for quote in quotes:
        title = quote.find_element(By.CSS_SELECTOR, "span.text").text.strip()
        author_name = quote.find_element(By.CSS_SELECTOR, "small.author").text.strip()

        tags = []
        for tag in quote.find_elements(By.CSS_SELECTOR, "a.tag"):
            tags.append(tag.text)

        all_data.append({
            "quote": title,
            "author": author_name,
            "tags": ", ".join(tags)
        })

    try:
        next_button = driver.find_element(By.CSS_SELECTOR, "li.next a")
        if next_button.is_displayed():
            next_button.click()
    except Exception as e:
        break

driver.close()


# Convert to DataFrame
df = pd.DataFrame(all_data)

# Save to CSV
df.to_csv("quotes.csv", index=False, encoding="utf-8")

print("Data saved to quotes.csv")