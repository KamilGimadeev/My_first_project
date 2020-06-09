from .pages.main_page import MainPage
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.base_page import BasePage
import pytest
import time
from selenium.webdriver.support.ui import WebDriverWait
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
   link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/'
   page = ProductPage(browser,link)
   page.open()
   prod = page.add_in_bascket()
   page.checking_additions(prod)
@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/'
    page = ProductPage(browser,link)
    page.open()
    page.add_in_bascket()
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/'
    page = ProductPage(browser,link)
    page.open()
    page.should_not_be_success_message()
@pytest.mark.need_review
@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/'
    page = ProductPage(browser,link)
    page.open()
    page.add_in_bascket()
    page.should_not_be_success_message_disappear()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self,browser):
        link = 'http://selenium1py.pythonanywhere.com/ru/'
        email = str(time.time()) + "@fakemail.org"
        password = 'gfhjkmvytytbpdtcnysq'
        page=LoginPage(browser,link)
        page.open()
        page.go_to_login_page()
        page.register_new_user(email,password)
        page.should_be_authorized_user()
    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self,browser):
       link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/'
       page = ProductPage(browser,link)
       page.open()
       prod = page.add_in_bascket()
       page.checking_additions(prod)
    @pytest.mark.xfail
    def test_user_cant_see_success_message_after_adding_product_to_basket(self,browser):
        link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/'
        page = ProductPage(browser,link)
        page.open()
        page.add_in_bascket()
        page.should_not_be_success_message()
