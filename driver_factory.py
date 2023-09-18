from selenium import webdriver

class DriverFactory:
    @staticmethod
    def create_chrome_driver():
        return webdriver.Chrome()

    @staticmethod
    def create_firefox_driver():
        return webdriver.Firefox()

    @staticmethod
    def create_edge_driver():
        return webdriver.Edge()

    def create_driver(browser_name):
        if browser_name.lower() == 'chrome':
            return DriverFactory.create_chrome_driver()
        elif browser_name.lower() == 'firefox':
            return DriverFactory.create_firefox_driver()
        elif browser_name.lower() == 'edge':
            return DriverFactory.create_edge_driver()
        else:
            raise ValueError("Unsupported browser: " + browser_name)
