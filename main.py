# imports --------------------------------------------------------------------#
from time import sleep

import winsound

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
from selenium.common.exceptions import NoSuchElementException
import pyautogui
import gspread
from gspread import Client, Spreadsheet, Worksheet

import defs.esc
from defs import read_tables
from defs.login import login
from selenium.webdriver.common.by import By

# ----------------------------------------------------------------------------#
global equipments, originalnosty, materials, status


def main():
    #----------------------------------------------------------------------------#
    photopath = None
    file_names = None
    select_category = None
    object_prices = None
    object_discriptions = None
    object_tags = None
    category_names = None
    equipments = None
    originalnosty = None
    materials = None
    status = None

    j = 1
    i = 1
    l = 1

    sh = read_tables.main()
    sheet_temp = sh.sheet1.col_values(1)
    #----------------------------------------------------------------------------#

    with open(".\photoPath.txt", 'r', encoding="UTF-8") as photofile:
        photopath = photofile.read() + "\\"
        print(photopath)
    #options.add_argument("--headless")  # Запуск браузера в режиме без головы
    driver = webdriver.Chrome()
    driver.get("https://minifreemarket.com/cabinet/products/add")
    sleep(1)
    login(driver)
    driver.get("https://minifreemarket.com/cabinet/products/add")
# ------------------------------------------------------------------------------------------------------------------------#
    file_names = read_tables.getFileName(sh)
    object_prices = read_tables.getFilePrice(sh)
    object_discriptions = read_tables.getFileDiscript(sh)
    object_tags = read_tables.getFileTags(sh)
    category_names = read_tables.getCategory(sh)
    sub_category_names = read_tables.getSubCategory(sh)
    group_names = read_tables.getGroup(sh)
    equipments = read_tables.getEquipment(sh)
    originalnosty = read_tables.getOriginal(sh)
    materials = read_tables.getMaterial(sh)
    status = read_tables.getStatus(sh)
#------------------------------------------------------------------------------------------------------------------------#
    while sheet_temp[j] != None:
        input(photopath, driver, equipments, originalnosty, materials, status, sh, j,
        file_names, object_prices, object_discriptions, object_tags, category_names, sub_category_names, group_names)
        j += 1
        driver.get("https://minifreemarket.com/cabinet/products/add")
        select_category = Select(
            driver.find_element(By.CLASS_NAME, 'product_change_cat.first_cat.select2-hidden-accessible'))

        div_elements = driver.find_elements(By.CSS_SELECTOR, 'div.uploded_img.add')
        upload_btn = None
        # Выводим все найденные элементы
        for i, div_element in enumerate(div_elements):
            if div_element.get_attribute('class'):
                upload_btn = div_element
                upload_btn.click()
                defs.esc.esc()

        submit_btn = driver.find_element(By.CSS_SELECTOR, "a.btn.submit")
        auction_btn = driver.find_element(By.CSS_SELECTOR, "a[data-val='auc']")
        auction_btn.click()
#------------------------------------------------------------------------------------------------------------------------#

def input(photopath, driver, equipments, originalnosty, materials, status, sh, i,
    object_names, object_prices, object_discriptions, object_tags, category_names, sub_category_names, group_names):
    temp = i
    object_name = object_names[i]
    object_tag = object_tags[i]
    object_discription = object_discriptions[i]
    object_price = object_prices[i]
    category_name = category_names[i].replace("_"," ")
    print(category_name)
    sub_category = sub_category_names[i].replace("_"," ")
    print(sub_category)
    group_name = group_names[i].replace("_"," ")
    print(group_name)
    if(category_name == "Экшен фигурки"):
        category_name = "Экшен-фигурки"
    div_elements = driver.find_elements(By.CSS_SELECTOR, 'div.uploded_img.add')
    submit_btn = driver.find_element(By.CSS_SELECTOR, "a.btn.submit")
    auction_btn = driver.find_element(By.CSS_SELECTOR, "a[data-val='auc']")
    auction_btn.click()

    for i, div_element in enumerate(div_elements):
        if div_element.get_attribute('class'):
            upload_btn = div_element
            upload_btn.click()
            defs.esc.esc()

    sleep(2)
    sh = read_tables.main()
    sheet_temp = sh.sheet1.col_values(1)
    select_category = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, f"//option[text()='{category_name}']"))
    )
    select_category.click()
    sub_select = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, f"//option[text()='{sub_category}']"))
    )
    sub_select.click()

    sleep(2)
    try:
        group_select = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, f"//option[text()='{group_name}']")))
        print(group_name)
        group_select.click()
    except TimeoutException:
        print(f"не найден элемент за выделенное время")
    sleep(2)
    try:
        equip_select = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, f"//option[text()='{equipments[temp]}']"))
        )
        equip_select.click()
        print(equipments[temp])
    except TimeoutException:
        print(f"не найден элемент за выделенное время")
    sleep(2)
    try:
        orig_select = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, f"//option[text()='{originalnosty[temp]}']"))
        )
        orig_select.click()
        print(originalnosty[temp])
    except TimeoutException:
        print(f"не найден элемент за выделенное время")
    sleep(2)
    try:
        mat_select = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, f"//option[text()='{materials[temp]}']"))
        )
        mat_select.click()
        print(materials[temp])
    except TimeoutException:
        print(f"не найден элемент за выделенное время")
    sleep(2)
    try:
        stat_select = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, f"//option[text()='{status[temp]}']"))
        )
        print(status[temp])
    except TimeoutException:
        print(f"не найден элемент за выделенное время")
    stat_select.click()
    sleep(2)

    inputs = driver.find_elements(By.TAG_NAME, 'input')
    input = inputs[8]
    file1 = f"{photopath}\{object_name} (1).jpg"
    file2 = f"{photopath}\{object_name} (2).jpg"
    file3 = f"{photopath}\{object_name} (3).jpg"
    file4 = f"{photopath}\{object_name} (4).jpg"
    file5 = f"{photopath}\{object_name} (5).jpg"
    has_file = [True, False, False, False, False]
    try:
        # Открываем файл
        file = open(file1, 'r')
        # Читаем содержимое файла
        content = file.read()
    except FileNotFoundError:
        print("Файл не найден.")
        return
    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")

    try:
        # Открываем файл
        file = open(file2, 'r')
        has_file[1] = True
        content = file.read()
    except FileNotFoundError:
        print("Файл не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")

    try:
        # Открываем файл
        file = open(file3, 'r')
        has_file[2] = True
        content = file.read()
    except FileNotFoundError:
        print("Файл не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")

    try:
        # Открываем файл
        file = open(file4, 'r')
        has_file[3] = True
        content = file.read()
    except FileNotFoundError:
        print("Файл не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")

    try:
        # Открываем файл
        file = open(file5, 'r')
        has_file[4] = True
        content = file.read()
        # Читаем содержимое файла
    except FileNotFoundError:
        print("Файл не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")

    true_count = has_file.count(True)

    files = [file1, file2, file3, file4, file5]
    for i in range(true_count):
        sleep(5)
        upload_file(files[i], driver)
    name_input = None
    inputs = driver.find_elements(By.TAG_NAME, 'input')
    name_input = inputs[6]
    name_input.send_keys(object_name)
    for inp in inputs:
        if 'Стартовая цена' in inp.get_attribute('placeholder'):
            input = inp
    input.clear()
    input.send_keys(object_price)
    input = driver.find_element(By.TAG_NAME, 'textarea')
    input.send_keys(object_discription)

    for inp in inputs:
        if 'Теги через запятую' in inp.get_attribute('placeholder'):
            input = inp
    input.send_keys(object_tag)
    #submit_btn.click()
    #driver.switch_to.alert.accept()
    #driver.refresh()

def upload_file(file, driver):
    inputs = driver.find_elements(By.TAG_NAME, 'input')
    input = inputs[8]
    print(input.get_attribute('class'))
    input.send_keys(file)
    div_elements = driver.find_elements(By.CSS_SELECTOR, 'div.uploded_img.add')
    sleep(2)
    sleep(2)

    # Выводим все найденные элементы
    for l, div_element in enumerate(div_elements):
        if div_element.get_attribute('class'):
            upload_btn = div_element
            sleep(5)
            try:
                upload_btn.click()
            except ElementClickInterceptedException:
                print('пиздец')
            defs.esc.esc()
            sleep(2)

if __name__ == "__main__":
    main()
