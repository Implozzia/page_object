from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_be_products_at_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.CHECKOUT_BTN), \
            "Have a checkout btn, but should not be"

    def should_be_empty_basket_text(self):
        assert "Your basket is empty." in self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_MSG).text, \
            "Do not have empty basket msg, but should be"