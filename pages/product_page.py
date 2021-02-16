from .base_page import BasePage
from .locators import BasketPageLocators


class ProductPage(BasePage):
    def should_be_add_to_basket_btn(self):
        assert self.is_element_present(*BasketPageLocators.ADD_TO_BASKET_BTN), "add to busket btn is not presented"

    def add_to_basket(self):
        basket_btn = self.browser.find_element(*BasketPageLocators.ADD_TO_BASKET_BTN)
        basket_btn.click()

    def should_be_equal_url(self):
        alert_name = self.browser.find_element(*BasketPageLocators.NAME_IN_ALERT).text
        product_name = self.browser.find_element(*BasketPageLocators.PRODUCT_NAME).text
        assert alert_name == product_name, "Product name didnt match"