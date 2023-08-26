from elements.button import Button
from .base_page import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    '''Главная страницы'''
    UNIQUE_LOCATOR = (By.ID, 'identifierNext')
    AUTH_BUTTON_LOCATOR = (By.ID, 'ddd')

    def __init__(self, driver):
        super().__init__(driver=driver,
                         unique_by_locator=self.UNIQUE_LOCATOR,
                         name='Main Page',
                         url='some_url')
        self.search_button = Button(driver=driver, by_locator=self.AUTH_BUTTON_LOCATOR, name='Auth Button')

    def fill_search_form(self, value):
        self.search_form.send_keys()
