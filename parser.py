import requests
from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def search_in_wb(search_words):
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1366,768")
    options.add_argument("user-agent=Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0")
    options.add_argument("--disable-blink-features=AutomationControlled")
    driver = webdriver.Chrome(
        executable_path="C:/chromedriver.exe",
        options=options
    )
    driver.get('https://www.wildberries.ru/')
    sleep(2)
    search = driver.find_element(By.CSS_SELECTOR, '#searchInput')
    search.send_keys(search_words)
    search.send_keys(Keys.ENTER)
    sleep(1)

# driver.implicitly_wait(10)
# button_apply = driver.find_element(By.XPATH, '//*[@id="applySearchBtn"]').click()
# sleep(3)
# fast_view = driver.find_elements((By.CLASS_NAME, 'product-card__fast-view'))
# print(fast_view)
# url = driver.current_url
# r = requests.get(url)
# # print(r)
# data = r.text
# soup = BeautifulSoup(data, 'lxml')
# cart = soup.find('div', class_='main__container')
# content = soup.find(id='catalog-content')
# print(content)
# item = driver.find_element(By.XPATH, '//*[@id="c39313886"]/div/a')
# link = item.get_attribute('href')
# article = link.split(sep = '/', maxsplit = -1)[4]
# print(article)

items = driver.find_elements(By.CLASS_NAME, 'product-card__main')
article_list = []
for i in items:
    link = i.get_attribute('href')
    article = link.split(sep = '/', maxsplit = -1)[4]
    article_list.append(article)
print(article_list)