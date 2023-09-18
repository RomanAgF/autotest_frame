import pytest
from selenium import webdriver
from pages.main_page import MainPage
# from json_reader import read_json_file, write_json_file #импортируем модуль json_reader
# data = read_json_file('json_data/config.json') # вызываем функцию read_json_file из модуля json_reader и читает JSON-данные из файла 'json_data/config.json' в переменную data
# from driver_factory import DriverFactory
#
# # Создаем экземпляр драйвера Chrome
# driver = DriverFactory.create_driver('chrome')
def test_fill_search_and_click(browser): # при каждом новом тесте пишем название функции и указываем обязателььно арг-т browser
    main_page = MainPage(browser) # cоздаем экземпляр страницы и дальше указываем нужные нам действия
    main_page.open()  # Открываем главную страницу

   # Заполняем поле поиска и нажимаем кнопку "поиск"
   #  time.sleep(5)
    search_text_mail = "testmail@gmail.com"
    main_page.fill_search_form_mail(search_text_mail)
    # time.sleep(5)  # Даем странице время загрузиться
    search_text_pass = "123456789"
    main_page.fill_search_form_pass(search_text_pass)
    # time.sleep(4)
    main_page.click_search_button()
    # time.sleep(5)  # Подождем, чтобы увидеть результат