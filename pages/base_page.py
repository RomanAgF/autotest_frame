from abc import ABC, abstractmethod
from  selenium.common.exceptions import NoSuchElementException
from driver.waits import Wait

class BasePage(ABC):
    ''''Базовый класс страницы'''

    @abstractmethod # чтобы нельзя было создать экземпляр BasePage
    def __init__(self, driver, unique_by_locator: tuple, name, url): # проверяем открылась ли страница по локатору
        self.driver = driver
        self.unique_by_locator = unique_by_locator
        self.name = name
        self.url = url
        self.wait = Wait(driver)

    def open(self):
        self.driver.get(self.url)

    def is_page_opened(self):
        try:
            element = self.wait.waitelemenetspreview(*self.unique_by_locator)
            return element.is_displayed() # реализовать, is_displayed вернет True или False
        except NoSuchElementException:
            return False


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