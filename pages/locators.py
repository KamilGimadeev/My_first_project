from selenium.webdriver.common.by import By
class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    SHOW_BASKET = (By.CSS_SELECTOR, '.btn-group  a.btn.btn-default')
    USER_ICON = (By.CSS_SELECTOR, '.icon-user')
class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    LOG_USERNAME = (By.NAME, 'login-username')
    LOG_PASSWORD = (By.NAME, 'login-password')
    REG_USERNAME = (By.CSS_SELECTOR, '#id_registration-email')
    REG_PASSWORD = (By.CSS_SELECTOR, '#id_registration-password1')
    REG_CONFIRM_PASSWORD = (By.CSS_SELECTOR, '#id_registration-password2')
    REG_BUTTON = (By.CSS_SELECTOR, '[name=registration_submit]')

class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, '.btn-add-to-basket')
    PRICE = (By.CSS_SELECTOR, '.price_color')
    BASKET = (By.CSS_SELECTOR, '.basket-mini')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main h1')
    MESSAGE = (By.CSS_SELECTOR, '.alertinner>strong')

class BasketPageLocators():
    EMPTY_MESSAGE = (By.CSS_SELECTOR, '#content_inner p')
    BASKET_ITEMS = (By.CSS_SELECTOR, '.basket-items')
