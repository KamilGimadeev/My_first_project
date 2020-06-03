from .locators import BasketPageLocators
from .base_page import BasePage


class BasketPage(BasePage):
    def missing_product_in_basket_show_message(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_MESSAGE) , 'No message of Basket is empty'

    def missing_product_in_basket_no_items(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS) , 'Exist product in Basket'
