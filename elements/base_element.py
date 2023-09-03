from abc import ABC, abstractmethod
from driver.waits import Wait

class BaseElement(ABC):

    @abstractmethod
    def __init__(self, driver, by_locator, name):
        self.by_locator = by_locator
        self.driver = driver
        self.name = name
        self.wait = Wait(driver)
    def click(self):
        element = self.wait.waitelemenetspreview(*self.by_locator) # ищем элемент на странице по локатору
        element.click() # кликаем по нему