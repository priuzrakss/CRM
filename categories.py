from time import sleep

import selenium
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from defs import login

options = Options()
#options.add_argument("--headless")  # Запуск браузера в режиме без головы
driver = webdriver.Chrome(options=options)
driver.get("https://minifreemarket.com/cabinet/products/add")
login.login(driver)
sleep(5)
driver.get("https://minifreemarket.com/cabinet/products/add")
categories = driver.find_elements(By.CLASS_NAME, 'option')
for cat in categories:
    print(categories[cat].get_attribute('data-value'))