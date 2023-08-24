import time
from .main_page import MainPage
from .email_page import EmailPage
from .password_page import PasswordPage
from .smart_page import SmartPage

class AuthPage(SmartPage):
    def __init__(self, driver):
        self.driver = driver
        self.main_page = MainPage(self.driver)
        self.main_page.load()  # Загружаем начальную страницу

    def get_expected_title(self):
        return 'Авторизация в Battle.net'

    def get_expected_final_title(self):
        return 'Обзор учетной записи'

    def login_google(self, email, password):
        '''Аутентификация через Google по данным пользователя'''
        # Вход через Google
        assert self.is_loaded()
        # time.sleep(5)
        self.main_page.click_google()
        # time.sleep(5)
        # Ввод электронной почты
        login_page = EmailPage(self.driver)
        login_page.set_email(email)
        # time.sleep(5)
        login_page.confirm()
