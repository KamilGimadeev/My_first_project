from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
# def test_guest_can_go_to_login_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/"
#     page = MainPage(browser,link)
#     page.open()
#     page.go_to_login_page()
#     login_page = LoginPage(browser,browser.current_url)
#     login_page.should_be_login_page()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/"
    page = BasketPage(browser, link)
    page.open()
    page.basket_showed()
    page.missing_product_in_basket_show_message()
    page.missing_product_in_basket_no_items()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/"
    page = BasketPage(browser, link, 1)
    page.open()
    page.basket_showed()
    page.missing_product_in_basket_show_message()
    page.missing_product_in_basket_no_items()
