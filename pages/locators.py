from selenium.webdriver.common.by import By
class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')

class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, '.btn-add-to-basket')
    PRICE = (By.CSS_SELECTOR, '.price_color')
    BASKET = (By.CSS_SELECTOR, '.basket-mini')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main h1')
    MESSAGE = (By.CSS_SELECTOR, '.alertinner>strong')
