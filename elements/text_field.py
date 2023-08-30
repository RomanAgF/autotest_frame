from elements.base_element import BaseElement


class TextField(BaseElement):

    def __init__(self, driver, by_locator, name):
        super().__init__(driver=driver, by_locator=by_locator, name=name)

    def send_text(self, text):
        element = self.driver.find_element(*self.by_locator)
        element.clear() # очистка поля ввода, если есть введенный ранее текст
        element.send_keys(text) # ввести текст в поле ввода
