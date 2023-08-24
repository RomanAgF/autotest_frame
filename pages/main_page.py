from .base_page import BasePage
from elements.main_page_elements import MainPageElements

class MainPage(BasePage):
    '''Главная страницы'''
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://eu.account.battle.net/login/ru/"
        self.elements = MainPageElements # Получаем нужыне элементы со страницы

    def load(self):
        self.driver.get(self.url)

    def click_google(self):
        self.driver.find_element(*self.elements.GOOGLE_BUTTON).click()

    def set_email(self, email):
        pass

    def set_password(self, password):
        pass

    def confirm(self):
        pass