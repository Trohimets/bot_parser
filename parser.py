import logging

from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException


logging.basicConfig(
    level=logging.DEBUG,
    filename='main.log',
    filemode='w',
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


options = webdriver.ChromeOptions()
options.add_argument("--window-size=1366,768")
options.add_argument("user-agent=Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0")
options.add_argument("--disable-blink-features=AutomationControlled")
driver = webdriver.Chrome(
    executable_path="chromedriver.exe",
    options=options
    )


def search_in_wb(search_words):
    try:
        driver.get('https://www.wildberries.ru/')
        sleep(3)
        button_search = driver.find_element(By.CSS_SELECTOR, '#searchInput')
        button_search.send_keys(search_words)
        button_search.send_keys(Keys.ENTER)
        sleep(4)
    except StaleElementReferenceException:
        logging.error(StaleElementReferenceException, exc_info=True)


def find_item_in_page(article):
    items = driver.find_elements(By.CLASS_NAME, 'product-card__main')
    article_list = []
    for i in items:
        link = i.get_attribute('href')
        article_item = link.split(sep = '/', maxsplit = -1)[4]
        article_list.append(article_item)
        if article_item == article:
            return len(article_list)
    return (-1)


def find_in_all_pages(article):
    for i in range(100):
        index = find_item_in_page(article)
        if index == -1:
            try:
                driver.find_element(By.CLASS_NAME, 'pagination-next').click()
                sleep(2)
            except Exception as E:
                logging.error(E, exc_info=True)
                return ("Произошла ошибка. Возможно, низкая скорость интернета")
        else:
            return (f'позиция товара на странице {i+1}: {index}')
    return ("Кажется, вашего товара нет в выдаче")
