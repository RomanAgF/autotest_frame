import pytest
from selenium import webdriver

@pytest.fixture(scope='function')
def browser():
    '''Подготовка к тестированию'''
    driver = webdriver.Firefox()  # инициализация вебдрайвера (перед тестами)
    yield driver
    driver.quit()  # завершение сессии (после тестов)
