from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        basket_button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        basket_button.click()

    def should_be_message_about_adding(self):
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        add_message = self.browser.find_element(*ProductPageLocators.ADD_MESSAGE).text
        assert book_name == add_message, 'Not book name in the message'

    def should_be_message_basket_total(self):
        book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
        price_message = self.browser.find_element(*ProductPageLocators.PRICE_MESSAGE).text
        assert book_price == price_message, 'Book prise != price in the message'

    def should_disappear_of_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.ADD_MESSAGE), \
            "Success message not disappear, but should be"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ADD_MESSAGE), \
            "Success message is presented, but should not be"
