from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.common.exceptions import NoSuchElementException
import pandas as pd

driver = webdriver.Chrome()

base_url = "https://books.toscrape.com/catalogue/page-{}.html"
page = 1

all_data = []

rating_dict = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}
while True:

    url = base_url.format(page)
    driver.get(url)

    books = driver.find_elements(By.CSS_SELECTOR, "ol.row li")
    
    if not books:
        print("No more pages found. Done.")
        break
    
    links = [book.find_element(By.CSS_SELECTOR, "h3 a").get_attribute("href") for book in books]

    for link in links:
        driver.get(link)
        driver.implicitly_wait(2)

        try:
            title = driver.find_element(By.CSS_SELECTOR,"div.product_main h1").text.strip()
            price = driver.find_element(By.CSS_SELECTOR, "p.price_color").text.strip()
            description = driver.find_element(By.CSS_SELECTOR, "div#product_description + p").text.strip()
            rating_class = driver.find_element(By.CSS_SELECTOR, "p.star-rating").get_attribute("class").split()[-1]
            rating = rating_dict.get(rating_class, 0)

            upc = driver.find_element(By.CSS_SELECTOR, "table.table.table-striped tbody tr:nth-child(1) td").text.strip()
            product_type = driver.find_element(By.CSS_SELECTOR, "table.table.table-striped tbody tr:nth-child(2) td").text.strip()
            price_excl_tax = driver.find_element(By.CSS_SELECTOR, "table.table.table-striped tbody tr:nth-child(3) td").text.strip()
            price_incl_tax = driver.find_element(By.CSS_SELECTOR, "table.table.table-striped tbody tr:nth-child(4) td").text.strip()
            tax = driver.find_element(By.CSS_SELECTOR, "table.table.table-striped tbody tr:nth-child(5) td").text.strip()
            availability = driver.find_element(By.CSS_SELECTOR, "table.table.table-striped tbody tr:nth-child(6) td").text.strip().split('(')[1].split()[0]
            num_of_reviews = driver.find_element(By.CSS_SELECTOR, "table.table.table-striped tbody tr:nth-child(7) td").text.strip()

            data = {
                "Title": title,
                "Price": price,
                "Rating": rating,
                "Description": description,
                "UPC": upc,
                "Product Type": product_type,
                "Price (Excl Tax)": price_excl_tax,
                "Price (Incl Tax)": price_incl_tax,
                "Tax": tax,
                "Availability": availability,
                "Number of Reviews": num_of_reviews,
                "URL": link
            }

            all_data.append(data)

            print("\n" + "="*60)
            for key, value in data.items():
                print(f"{key:<20}: {value}")
            print("="*60)
        except Exception as e:
            print("Error:", e)

    print("\n" + "*"*50 + "\n")

    page += 1

driver.quit()

df = pd.DataFrame(all_data)
df.to_csv("books_data.csv", index=False, encoding="utf-8")

print("\nData saved to books_data.csv")