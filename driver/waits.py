from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Wait:
    def __init__(self, driver):
        self.driver = driver

    def waitelemenetspreview(self, by_locator, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        elem = wait.until(EC.presence_of_element_located(by_locator))
        return elem
