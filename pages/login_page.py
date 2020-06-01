from .base_page import BasePage
from .locators import LoginPage

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert 'LOGIN' in upper(self.browser.current_url) , 'Url not contained login'

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert is_element_present(*LoginPage.LOGIN_FORM) , 'Login form exist'

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert is_element_present(*LoginPage.REGISTER_FORM) , 'Login form exist'
