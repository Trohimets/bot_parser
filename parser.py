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
# driver.implicitly_wait(10)
search.send_keys('Омега')
search.send_keys(Keys.ENTER)
sleep(2)
# button_apply = driver.find_element(By.XPATH, '//*[@id="applySearchBtn"]').click()
# sleep(3)
soup = BeautifulSoup(driver.page_source, 'lxml')
content = soup.find(id='catalog-content').text
print(content)