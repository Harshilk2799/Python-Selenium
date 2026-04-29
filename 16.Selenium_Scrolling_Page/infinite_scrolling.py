from selenium import webdriver
from selenium.webdriver.common.by import By 
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.google.com/search?sca_esv=00e10f0057297768&sxsrf=ANbL-n4XJ54OC4oEuhfSrq0312GpJCvWWA:1776342985021&udm=2&fbs=ADc_l-aN0CWEZBOHjofHoaMMDiKpaEWjvZ2Py1XXV8d8KvlI3o6iwGk6Iv1tRbZIBNIVs-7DjmheGwJ9kkYLzOq5Q2x5_vUa7NlVh74273t1qYj0GD1vkYVaFIvIYcBAr4Up4b-5fwwevOzkL70zu1rZXIG3kdV2jyLDZJa2J4VgROT2n6_iW7H2bpng4BUOszKY5mOFMmbjCYZf_3N0Gli1-IlKr3WLkQ&q=python&sa=X&ved=2ahUKEwjijfyksfKTAxXKyzgGHW-VJoUQtKgLegQIEhAB&biw=1294&bih=620&dpr=1")
time.sleep(2)

prev_height = driver.execute_script("return document.body.scrollHeight;")
while True:
    print(f"Webpage height: {prev_height} pixels")
    
    # scroll to page bottom 
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait for content load
    time.sleep(3)

    new_height = driver.execute_script("return document.body.scrollHeight;")

    if prev_height == new_height:
        break

    prev_height = new_height