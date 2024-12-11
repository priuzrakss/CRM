<<<<<<< HEAD
import os
from time import sleep
import time
import defs.esc
from defs import read_tables
from defs.login import login
import pandas as pd
from selenium import webdriver


categories = {
        "Коллекционные карточные игры": [
            "Аксессуары для ККИ",
            "Берсерк. Герои",
            "Классический Берсерк",
            "Прочие карточные игры",
            "Cardfight!! Vanguard",
            "KeyForge",
            "Magic: The Gathering",
            "Pokemon",
            "Star Wars Destiny",
            "World Of Warcraft"
        ],
        "Ролевые игры": [
            "Аксессуары для ролевых игр",
            "Модели для ролевых игр",
            "Прочие НРИ",
            "Dungeons & Dragons",
            "Pathfinder"
        ],
        "Настольные игры": [
            "Аксессуары для настольных игр"
            "Детективные игры",
            "Игры для вечеринок",
            "Карточные игры",
            "Кооперативные игры",
            "Настольные игры для детей",
            "Стратегические игры",
            "Экономические игры"
        ],
        "Все для моделирования": [
            "Дополнения для моделизма",
            "Кисти",
            "Краски",
            "Материалы для моделирования",
            "Рабочий инструмент",
            "Системы хранения",
            "Химия"],
        "Стендовые модели": [
            "Бюсты",
            "Военная авиация",
            "Военная техника",
            "Гражданская авиация",
            "Гражданская техника",
            "Диорамы",
            "Пехота и кавалерия",
            "Прочие стендовые модели",
            "Флот",
        ],
        "Варгеймы": [
            "Авторские варгеймы",
            "Авторские миниатюры",
            "Аксессуары",
            "Наполеоника, Black Powder",
            "Песнь Льда и Огня",
            "Прочие игры с миниатюрами",
            "Террейн",
            "Технолог",
            "Batman Miniature Game",
            "BattleTech",
            "Dark Lands",
            "Dropfleet Commander",
            "Dropzone Commander",
            "Fallout: Wasteland Warfare",
            "Guild Ball",
            "Harry Potter Miniatures Adventure Game",
            "Infinity The Game",
            "Legends of Signum",
            "Malifaux",
            "Marvel Crisis Protocol",
            "Rackham Confrontation",
            "SAGA",
            "Star Wars",
            "The Elder Scrolls: Call to Arms",
            "Warhammer 40.000",
            "Warhammer Age of Sigmar",
            "Warhammer The Old World",
            "Warmachine and Hordes",
            "Wild West Exodus",
        ],
        "Печать 3D миниатюр": ["Печать 3D миниатюр"]
        # Добавьте остальные категории аналогичным образом
    }

def main():
    start_time = time.time()
    sh = read_tables.main()
    sheet_temp = sh.sheet1.col_values(1)

    names = read_tables.getFileName(sh)
    price = read_tables.getFilePrice(sh)
    discript = read_tables.getFileDiscript(sh)
    tags = read_tables.getFileTags(sh)
    sub_category = read_tables.getCategory(sh)
    complect = read_tables.getEquipment(sh)
    orig = read_tables.getOriginal(sh)
    material = read_tables.getMaterial(sh)
    status = read_tables.getStatus(sh)

    arrays = [names, price, discript,tags,sub_category, complect, orig, material, status]
    arrays = limit_array_lengths(arrays)

    df = pd.DataFrame({
        "Название продукта": arrays[0],
        "Цена": arrays[1],
        "Описание": arrays[2],
        "Теги": arrays[3],
        "Категория": find_category(arrays[4]),
        "Подкатегория": arrays[4],
        "Комплект": arrays[5],
        "Материал": arrays[7],
        "Оригинальность": arrays[6],
        "Состояние": arrays[7]
    })
    df.to_excel("startoutput.xlsx", index=False)  # Замените имя файла на нужное
    end_time = time.time()
    print(f"{end_time - start_time} - время выполнения")



def find_category(sub_category_name):
    for category, sub_categories in categories.items():
        if sub_category_name in sub_categories:
            return category
    return None


def limit_array_lengths(arrays):
    if not arrays:
        return arrays

    # Длина первого массива
    first_array_length = min(len(arr) for arr in arrays)

    # Проверка, все ли массивы одной длины
    all_same_length = all(len(arr) == first_array_length for arr in arrays)

    if all_same_length:
        return arrays
    else:
        # Ограничение длины всех массивов по длине первого массива
        return [arr[:first_array_length] for arr in arrays]

if __name__ == "__main__":
=======
import os
from time import sleep
import time
import defs.esc
from defs import read_tables
from defs.login import login
import pandas as pd
from selenium import webdriver


categories = {
        "Коллекционные карточные игры": [
            "Аксессуары для ККИ",
            "Берсерк. Герои",
            "Классический Берсерк",
            "Прочие карточные игры",
            "Cardfight!! Vanguard",
            "KeyForge",
            "Magic: The Gathering",
            "Pokemon",
            "Star Wars Destiny",
            "World Of Warcraft"
        ],
        "Ролевые игры": [
            "Аксессуары для ролевых игр",
            "Модели для ролевых игр",
            "Прочие НРИ",
            "Dungeons & Dragons",
            "Pathfinder"
        ],
        "Настольные игры": [
            "Аксессуары для настольных игр"
            "Детективные игры",
            "Игры для вечеринок",
            "Карточные игры",
            "Кооперативные игры",
            "Настольные игры для детей",
            "Стратегические игры",
            "Экономические игры"
        ],
        "Все для моделирования": [
            "Дополнения для моделизма",
            "Кисти",
            "Краски",
            "Материалы для моделирования",
            "Рабочий инструмент",
            "Системы хранения",
            "Химия"],
        "Стендовые модели": [
            "Бюсты",
            "Военная авиация",
            "Военная техника",
            "Гражданская авиация",
            "Гражданская техника",
            "Диорамы",
            "Пехота и кавалерия",
            "Прочие стендовые модели",
            "Флот",
        ],
        "Варгеймы": [
            "Авторские варгеймы",
            "Авторские миниатюры",
            "Аксессуары",
            "Наполеоника, Black Powder",
            "Песнь Льда и Огня",
            "Прочие игры с миниатюрами",
            "Террейн",
            "Технолог",
            "Batman Miniature Game",
            "BattleTech",
            "Dark Lands",
            "Dropfleet Commander",
            "Dropzone Commander",
            "Fallout: Wasteland Warfare",
            "Guild Ball",
            "Harry Potter Miniatures Adventure Game",
            "Infinity The Game",
            "Legends of Signum",
            "Malifaux",
            "Marvel Crisis Protocol",
            "Rackham Confrontation",
            "SAGA",
            "Star Wars",
            "The Elder Scrolls: Call to Arms",
            "Warhammer 40.000",
            "Warhammer Age of Sigmar",
            "Warhammer The Old World",
            "Warmachine and Hordes",
            "Wild West Exodus",
        ],
        "Печать 3D миниатюр": ["Печать 3D миниатюр"]
        # Добавьте остальные категории аналогичным образом
    }

def main():
    start_time = time.time()
    sh = read_tables.main()
    sheet_temp = sh.sheet1.col_values(1)

    names = read_tables.getFileName(sh)
    price = read_tables.getFilePrice(sh)
    discript = read_tables.getFileDiscript(sh)
    tags = read_tables.getFileTags(sh)
    sub_category = read_tables.getCategory(sh)
    complect = read_tables.getEquipment(sh)
    orig = read_tables.getOriginal(sh)
    material = read_tables.getMaterial(sh)
    status = read_tables.getStatus(sh)

    arrays = [names, price, discript,tags,sub_category, complect, orig, material, status]
    arrays = limit_array_lengths(arrays)

    df = pd.DataFrame({
        "Название продукта": arrays[0],
        "Цена": arrays[1],
        "Описание": arrays[2],
        "Теги": arrays[3],
        "Категория": find_category(arrays[4]),
        "Подкатегория": arrays[4],
        "Комплект": arrays[5],
        "Материал": arrays[7],
        "Оригинальность": arrays[6],
        "Состояние": arrays[7]
    })
    df.to_excel("startoutput.xlsx", index=False)  # Замените имя файла на нужное
    end_time = time.time()
    print(f"{end_time - start_time} - время выполнения")



def find_category(sub_category_name):
    for category, sub_categories in categories.items():
        if sub_category_name in sub_categories:
            return category
    return None


def limit_array_lengths(arrays):
    if not arrays:
        return arrays

    # Длина первого массива
    first_array_length = min(len(arr) for arr in arrays)

    # Проверка, все ли массивы одной длины
    all_same_length = all(len(arr) == first_array_length for arr in arrays)

    if all_same_length:
        return arrays
    else:
        # Ограничение длины всех массивов по длине первого массива
        return [arr[:first_array_length] for arr in arrays]

if __name__ == "__main__":
>>>>>>> 623c4009141dd713f3bb3f4e4ec9dba8c53103b4
    main()