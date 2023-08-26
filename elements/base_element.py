from abc import ABC, abstractmethod


class BaseElement(ABC):

    @abstractmethod
    def __init__(self, driver, by_locator, name):
        self.by_locator = by_locator
        self.driver = driver
        self.name = name

    def click(self):
        pass

