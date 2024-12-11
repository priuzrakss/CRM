from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By

from defs import logginIssue


def login(driver):
    # Создаем новый экземпляр Chrome WebDriver


    submit_button = None

    inputs = driver.find_elements(By.TAG_NAME, "input")
    elements = driver.find_elements(By.TAG_NAME, "a")
    # поиск кнопки входа
    for element in elements:
        # Если класс элемента совпадает с 'btn submit', то это искомый элемент
        if 'btn submit' in element.get_attribute('class'):
            submit_button = element

    # инициализация полей
    login_place = inputs[4]
    password_place = inputs[5]

    issue = logginIssue

    config_file_path = "logginIssue.json"
    credentials_manager = issue.CredentialsManager(config_file_path)
    credentials_manager.load_credentials()

    if credentials_manager.login is None or credentials_manager.password is None:
        print("Error: Missing login or password")
    else:
        print(f"Login: {credentials_manager.login}")
        print(f"Password: {credentials_manager.password}")

    # обработка полей
    login_place.send_keys(credentials_manager.login)
    password_place.send_keys(credentials_manager.password)

    # обработка кнопок
    submit_button.click()

# ----------------------------------------------------------------------------#
