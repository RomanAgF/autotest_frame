from pages.auth_page import AuthPage

def test_auth_page(browser):
    '''Тест на прохождение аутентификации'''
    auth_page = AuthPage(browser)
    auth_page.login_google('your_email@gmail.com', 'your_password')
