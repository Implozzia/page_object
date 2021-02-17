from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_add_to_basket_btn(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BTN), "add to busket btn is not presented"

    def add_to_basket(self):
        basket_btn = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN)
        basket_btn.click()

    def should_be_equal_url(self):
        alert_name = self.browser.find_element(*ProductPageLocators.NAME_IN_ALERT).text
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        assert alert_name == product_name, "Product name didnt match"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ALERT_SUCCESS), \
            "Success message is presented, but should not be"

    def should_dissapear_of_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.ALERT_SUCCESS), \
            "Success message is not dissapear, but should be"