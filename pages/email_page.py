from .base_page import BasePage
from elements.email_page_elements import EmailPageElements

class EmailPage(BasePage):
    '''Страница ввода электронной почты'''

    def __init__(self, driver):
        self.driver = driver
        self.elements = EmailPageElements  # Получаем нужные элементы страницы

    def set_email(self, email):
        self.driver.find_element(*self.elements.EMAIL_FIELD).send_keys(email)

    def confirm(self):
        self.driver.find_element(*self.elements.CONFIRM_BUTTON).click()

    def load(self):
        pass

    def click_google(self):
        pass
    def set_password(self, password):
        pass