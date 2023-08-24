from .base_page import BasePage
from elements.password_page_elements import PasswordPageElements

class PasswordPage(BasePage):
    '''Страница ввода пароля'''

    def __init__(self, driver):
        self.driver = driver
        self.elements = PasswordPageElements  # Получаем нужные элементы страницы

    def set_password(self, password):
        self.driver.find_element(*self.elements.PASSWORD_FIELD).send_keys(password)

    def confirm(self):
        self.driver.find_element(*self.elements.CONFIRM_BUTTON).click()

    def load(self):
        pass

    def click_google(self):
        pass

    def set_email(self, email):
        pass
