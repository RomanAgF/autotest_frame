from selenium.webdriver.common.by import By

class PasswordPageElements:
    '''Необходимые элементы страницы ввода пароля'''
    PASSWORD_FIELD = (By.ID, 'password')  # поле для ввода
    CONFIRM_BUTTON = (By.ID, 'passwordNext')  # кнопка "Далее"
