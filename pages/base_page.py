from abc import ABC, abstractmethod


class BasePage(ABC):
    ''''Базовый класс страницы'''

    @abstractmethod
    def __init__(self, driver, unique_by_locator: tuple, name, url):
        self.driver = driver
        self.unique_by_locator = unique_by_locator
        self.name = name
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def is_page_opened(self):
        element = self.driver.find_element(*unique_by_locator)
        return element.is_displayed()

    # @abstractmethod
    # def load(self):
    #     '''Загрузка страницы'''
    #     pass
    # @abstractmethod
    # def set_email(self, email):
    #     '''Ввод электронной почты в поле'''
    #     pass
    #
    # @abstractmethod
    # def set_password(self, password):
    #     '''Ввод пароля'''
    #     pass
    # @abstractmethod
    # def confirm(self):
    #     '''Нажатие далее'''
    #     pass
    #
    # @abstractmethod
    # def click_google(self):
    #     '''Нажатие вход черезе гугл аккаунт'''
    #     pass
