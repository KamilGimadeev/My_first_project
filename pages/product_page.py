from .base_page import BasePage
from .locators import ProductPageLocators
class ProductPage(BasePage):
    def add_in_bascket(self):
        name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        prodname = name.text
        link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        link.click()
        return prodname
    def checking_additions(self,prodname):
        product_price = self.browser.find_element(*ProductPageLocators.PRICE)
        a = product_price.text
        basket_summ = self.browser.find_element(*ProductPageLocators.BASKET)
        b = basket_summ.text
        mess = []
        mess = self.browser.find_elements(*ProductPageLocators.MESSAGE)
        mess0 = mess[0].text
        assert (a in b) and (prodname == mess0), 'Product was not added'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE), \
            "Success message is presented, but should not be"

    def should_not_be_success_message_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.MESSAGE), \
            "Element was not disappeared"
