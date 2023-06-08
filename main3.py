import time

import chromedriver_autoinstaller
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
chromedriver_autoinstaller.install()

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager(cache_valid_range=10).install()))
url = "https://webscraper.io/test-sites/e-commerce/scroll/computers/tablets"
driver.get(url)
driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
time.sleep(5)
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
prices = soup.find_all('h4', class_='pull-right price')
models = soup.find_all('a', class_='title')
for model, price in zip(models, prices):
    m = model.get_text()
    p = price.get_text()
    print(f'Товар {m}, цена - {p}')
