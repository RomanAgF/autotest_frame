from abc import ABC, abstractmethod

class SmartPage(ABC):
    def __init__(self, driver):
        self.driver = driver

    def is_loaded(self):
        '''Проверка на открытие нужной страницы'''
        expected_title = self.get_expected_title()
        if not expected_title:
            return True
        return expected_title == self.driver.title

    def is_authenticated(self):
        '''Проверка на успешное прохождение аутентификации'''
        expected_title = self.get_expected_final_title()
        if not expected_title:
            return True
        return expected_title == self.driver.title

    @abstractmethod
    def get_expected_title(self):
        '''Заголовок начальной страницы'''
        pass

    @abstractmethod
    def get_expected_final_title(self):
        '''Заголовок страницы после аутентификации'''
        pass
