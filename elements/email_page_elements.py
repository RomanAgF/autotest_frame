from selenium.webdriver.common.by import By


class EmailPageElements:
    '''Необходимые элементы страницы ввода электронной почты'''
    EMAIL_FIELD = (By.ID, 'identifierId')  # поле для ввода
    CONFIRM_BUTTON = (By.ID, 'identifierNext')  # кнопка "Далее"
