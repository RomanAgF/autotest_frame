from elements.button import Button
from elements.text_field import TextField
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
        self.auth_button = Button(driver=driver, by_locator=self.AUTH_BUTTON_LOCATOR, name='Auth Button')
        self.search_form = TextField(driver=driver, by_locator=self.SEARCH_FORM_LOCATOR, name='Search Form')
        self.search_button = TextField(driver=driver, by_locator=self.SEARCH_BUTTON_LOCATOR, name='Search Button')
    def fill_search_form(self, value):
        self.search_form.send_text(value)

    def click_search_button(self):
        self.search_button.click()



