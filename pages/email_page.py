from .base_page import BasePage
from elements.email_page_elements import EmailPageElements
from driver.waits import Wait
class EmailPage(BasePage):
    '''Страница ввода электронной почты'''

    def __init__(self, driver):
        self.driver = driver
        self.elements = EmailPageElements  # Получаем нужные элементы страницы
        self.wait = Wait(driver)
    def set_email(self, email):
        self.wait.waitelementspresence(*self.elements.EMAIL_FIELD).send_keys(email)
        element.send_keys(email)
    def confirm(self):
        self.wait.waitelementspresence(*self.elements.CONFIRM_BUTTON).click()
        element.click()
    def load(self):
        pass

    def click_google(self):
        pass
    def set_password(self, password):
        pass