from pages.auth_page import AuthPage
def test_login_page_opened(browser):
    '''Тест на корректное открытие главной страницы'''
    auth_page = AuthPage(browser)
    assert auth_page.is_loaded()
