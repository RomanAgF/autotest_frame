from elements.button import Button
from elements.text_field import TextField
from .base_page import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    '''Главная страницы'''
    UNIQUE_LOCATOR = (By.ID, 'identifierNext')
    AUTH_BUTTON_LOCATOR = (By.ID, 'ddd')
    SEARCH_FORM_LOCATOR = (By.ID, 'accountName')
    SEARCH_FORM_LOCATOR_PASS = (By.ID, 'password')
    SEARCH_BUTTON_LOCATOR = (By.ID, 'submit')
    def __init__(self, driver):
        # super().__init__(driver=driver,
        #                  unique_by_locator=self.UNIQUE_LOCATOR,
        #                  name='Main Page',
        #                  url='some_url')
        self.driver = driver
        self.unique_by_locator = self.UNIQUE_LOCATOR
        self.name = 'Main Page'
        self.url = 'https://eu.account.battle.net/login/ru/'
#----------------------------------------------------------------------------------------------------------------------#
        #self.auth_button = Button(driver=driver, by_locator=self.AUTH_BUTTON_LOCATOR, name='Auth Button')
        self.search_form_mail = TextField(driver=driver, by_locator=self.SEARCH_FORM_LOCATOR, name='Search Form') # поле ввода почты
        self.search_form_pass = TextField(driver=driver, by_locator=self.SEARCH_FORM_LOCATOR_PASS, name='Search Button') # поле ввода пароля
        self.search_button = Button(driver=driver, by_locator=self.SEARCH_BUTTON_LOCATOR, name='Search Button')  # кнопка авторизоваться



    def fill_search_form_mail(self, value):
        self.search_form_mail.send_text(value)

    def fill_search_form_pass(self, value):
        self.search_form_pass.send_text(value)

    def click_search_button(self):
        self.search_button.click()



