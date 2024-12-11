<<<<<<< HEAD
import os
import time
from time import sleep

import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from defs.login import login

start_time = time.time()
# Путь к файлу, который нужно удалить
file_path = "output.xlsx"
start_file_path = "output.xlsx"
# Удаление файла
try:
    os.chmod(file_path, 0o755)
    os.remove(file_path)
    os.remove(start_file_path)
    print(f"Файл {file_path} и {start_file_path} успешно удален.")
except FileNotFoundError:
    print(f"Файл {file_path} или {start_file_path}не найден.")
except PermissionError:
    print(f"Нет разрешения на удаление файла {file_path}.")

options = Options()
options.add_argument("--headless")  # Запуск браузера в режиме без головы
driver = webdriver.Chrome(options=options)
driver.get("https://minifreemarket.com/cabinet/products/add")
sleep(1)
login(driver)

# Открытие веб-страницы
driver.get("https://minifreemarket.com/cabinet/products?page=1&fi_auction=1")  # Замените URL на нужный
# Нахождение элементов на странице
product_titles = driver.find_elements(By.CLASS_NAME ,"product_title")
prices = driver.find_elements(By.CLASS_NAME ,"price")
col_actions_labels = driver.find_elements(By.CSS_SELECTOR ,".col_actions label")
element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "html")))
col_count = driver.find_elements(By.CLASS_NAME, "col_count")

titles_m = []
prices_m = []
col_actions_labels_m = []
col_count_m = []
i = 1
is_None = 0
while is_None == 0:

    product_titles = driver.find_elements(By.CLASS_NAME, "product_title")
    prices = driver.find_elements(By.CLASS_NAME, "price")
    col_actions_labels = driver.find_elements(By.CSS_SELECTOR, ".col_actions label")
    col_count = driver.find_elements(By.CLASS_NAME, "col_count")

    if(len(product_titles) == 0):
        is_None = 1
    for count in col_count:
        col_count_m.append(count.text)
        print("состояние: ", count.text)

    # Получение текста из элементов
    for title in product_titles:
        print("Название продукта:", title.text)

    for title in product_titles:
        titles_m.append(title.text)

    for label in col_actions_labels:
        print("Текст метки:", label.text)

    for label in col_actions_labels:
        col_actions_labels_m.append(label.text)



    filtered_prices = prices[1::2]
    for price in filtered_prices:
        string = price.text
        string = string.replace("e", " руб")
        print("Цена продукта:", string)
        price = string
    for price in filtered_prices:
        string = price.text
        string = string.replace("e", " руб")
        prices_m.append(string)
    i+=1
    driver.get(f"https://minifreemarket.com/cabinet/products?page={i}&fi_auction=1")  # Замените URL на нужный

df = pd.DataFrame({
    "Название продукта": titles_m,
    "Цена": prices_m,
    "Метка": col_actions_labels_m,
    "Состояние": col_count_m
})

# Сохранение в Excel
df.to_excel("output.xlsx", index=False)  # Замените имя файла на нужное

print("Данные успешно записаны в файл output.xlsx")
end_time = time.time()
print(f"{end_time - start_time} - время выполнения")
# Закрытие браузера
driver.quit()
=======
import os
import time
from time import sleep

import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from defs.login import login

start_time = time.time()
# Путь к файлу, который нужно удалить
file_path = "output.xlsx"
start_file_path = "output.xlsx"
# Удаление файла
try:
    os.chmod(file_path, 0o755)
    os.remove(file_path)
    os.remove(start_file_path)
    print(f"Файл {file_path} и {start_file_path} успешно удален.")
except FileNotFoundError:
    print(f"Файл {file_path} или {start_file_path}не найден.")
except PermissionError:
    print(f"Нет разрешения на удаление файла {file_path}.")

options = Options()
options.add_argument("--headless")  # Запуск браузера в режиме без головы
driver = webdriver.Chrome(options=options)
driver.get("https://minifreemarket.com/cabinet/products/add")
sleep(1)
login(driver)

# Открытие веб-страницы
driver.get("https://minifreemarket.com/cabinet/products?page=1&fi_auction=1")  # Замените URL на нужный
# Нахождение элементов на странице
product_titles = driver.find_elements(By.CLASS_NAME ,"product_title")
prices = driver.find_elements(By.CLASS_NAME ,"price")
col_actions_labels = driver.find_elements(By.CSS_SELECTOR ,".col_actions label")
element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "html")))
col_count = driver.find_elements(By.CLASS_NAME, "col_count")

titles_m = []
prices_m = []
col_actions_labels_m = []
col_count_m = []
i = 1
is_None = 0
while is_None == 0:

    product_titles = driver.find_elements(By.CLASS_NAME, "product_title")
    prices = driver.find_elements(By.CLASS_NAME, "price")
    col_actions_labels = driver.find_elements(By.CSS_SELECTOR, ".col_actions label")
    col_count = driver.find_elements(By.CLASS_NAME, "col_count")

    if(len(product_titles) == 0):
        is_None = 1
    for count in col_count:
        col_count_m.append(count.text)
        print("состояние: ", count.text)

    # Получение текста из элементов
    for title in product_titles:
        print("Название продукта:", title.text)

    for title in product_titles:
        titles_m.append(title.text)

    for label in col_actions_labels:
        print("Текст метки:", label.text)

    for label in col_actions_labels:
        col_actions_labels_m.append(label.text)



    filtered_prices = prices[1::2]
    for price in filtered_prices:
        string = price.text
        string = string.replace("e", " руб")
        print("Цена продукта:", string)
        price = string
    for price in filtered_prices:
        string = price.text
        string = string.replace("e", " руб")
        prices_m.append(string)
    i+=1
    driver.get(f"https://minifreemarket.com/cabinet/products?page={i}&fi_auction=1")  # Замените URL на нужный

df = pd.DataFrame({
    "Название продукта": titles_m,
    "Цена": prices_m,
    "Метка": col_actions_labels_m,
    "Состояние": col_count_m
})

# Сохранение в Excel
df.to_excel("output.xlsx", index=False)  # Замените имя файла на нужное

print("Данные успешно записаны в файл output.xlsx")
end_time = time.time()
print(f"{end_time - start_time} - время выполнения")
# Закрытие браузера
driver.quit()
>>>>>>> 623c4009141dd713f3bb3f4e4ec9dba8c53103b4
