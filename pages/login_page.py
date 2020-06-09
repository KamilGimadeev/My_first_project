from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert 'login' in self.browser.current_url , 'Url not contained login'

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM) , 'Login form exist'

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM) , 'Login form exist'

    def register_new_user(self,email, password):
        registration_email = self.browser.find_element(*LoginPageLocators.REG_USERNAME)
        registration_email.send_keys(email)
        registration_password = self.browser.find_element(*LoginPageLocators.REG_PASSWORD)
        registration_password.send_keys(password)
        registration_confirm_password = self.browser.find_element(*LoginPageLocators.REG_CONFIRM_PASSWORD)
        registration_confirm_password.send_keys(password)
        button=self.browser.find_element(*LoginPageLocators.REG_BUTTON)
        button.click()
