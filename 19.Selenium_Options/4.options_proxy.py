from selenium.webdriver import ChromeOptions
from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType


options = ChromeOptions()

# ---- Method 1: Direct argument ----
options.add_argument("--proxy-server=http://proxy_host:8080")

# ---- Method 2: Proxy object ----
proxy = Proxy()
proxy.proxy_type = ProxyType.MANUAL
proxy.http_proxy = "proxy_host:8080"
proxy.ssl_proxy  = "proxy_host:8080"
options.proxy = proxy

# Modern headless (recommended for Chrome >= 112)
options.add_argument("--headless=new")
options.add_argument("--window-size=1920,1080")  # Important: set size in headless mode

driver = webdriver.Chrome(options=options)

# Launch Chrome with options
driver = webdriver.Chrome(options=options)
driver.get("https://quotes.toscrape.com/")
print(driver.title)
driver.quit()