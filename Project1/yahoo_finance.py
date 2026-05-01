import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
print("Hello")
wait = WebDriverWait(driver, 5)
driver.get("https://finance.yahoo.com/")
print("Hello")
# Wait for the webpage to load 
page_title = driver.title
print(page_title)
print("Hello")
try:
    print("Hello=====Try")
    wait.until(lambda d:d.execute_script("return document.readyState") == "interactive") 
    print("Hello====END TRY")
except Exception as e: 
    print(f"The page {page_title} did not get fully loaded within the given duration!")
else:
    print(f"The page {page_title} is fully loaded!")

# hovering on markets menu
actions = ActionChains(driver)

markets_menu = wait.until(
    EC.presence_of_element_located(By.XPATH, "//*[@id='navigation-container']/ol/li[3]/a/div")
)
actions.move_to_element(markets_menu).perform()

stocks_dropdown = wait.until(
    EC.presence_of_element_located(By.XPATH, "//*[@id='navigation-container']/ol/li[3]/ol/li[1]/a/span")
)
actions.move_to_element(stocks_dropdown).perform()

trending = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//*[@id='navigation-container']/ol/li[3]/ol/li[1]/ol/li[4]/a/span"))
)
actions.click(trending).perform()


# # Click on most active
most_active = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//*[@id='tab-most-active']"))
)
actions.click(most_active).perform()

# navigating the stocks pages
data = []

while True:
    # Scraping 
    wait.until(
        EC.presence_of_element_located((By.XPATH, "//table"))
    )
    
    records = driver.find_elements(By.XPATH, "//*[@id='main-content-wrapper'']/section[1]/div/div[3]/div/table/tbody/tr")

    print("Length: ", len(records))
    for record in records:
        cols = record.find_element(By.TAG_NAME, "td")

        if len(cols) >= 9:
            record = {
                "Symbol": cols[0].text,
                "Name": cols[1].text,
                "Price": cols[2].text,
                "Change": cols[3].text,
                "Change %": cols[4].text,
                "Volume": cols[5].text,
                "Avg Volume": cols[6].text,
                "Market Cap": cols[7].text,
                "PE Ratio": cols[8].text
            }
            data.append(record)

    print(f"Collected {len(data)} records so far...")

    # click next
    try:
        next_button = wait.until(
            EC.element_to_be_clickable(By.XPATH, "//*[@id='tab-most-active']")
        )
    except Exception as e:
        print("The next button is not clickable. We have navigated through all the pages.")
        break
    else:
        actions.click(next_button).perform()
        time.sleep(2)

# df = pd.DataFrame(data)
# df.to_excel("yahoo_most_active.xlsx", index=False)

# print("Data saved to yahoo_most_active.xlsx")

driver.quit()