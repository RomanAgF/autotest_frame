from elements.base_element import BaseElement


class Button(BaseElement):

    def __init__(self, driver, by_locator, name):
        super().__init__(driver=driver, by_locator=by_locator, name=name)
