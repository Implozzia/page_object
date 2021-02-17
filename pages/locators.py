from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.LINK_TEXT, "View basket")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    CHECKOUT_BTN = (By.CSS_SELECTOR, '.btn-primary')
    EMPTY_BASKET_MSG = (By.CSS_SELECTOR, '#content_inner p')


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REG_FORM = (By.CSS_SELECTOR, '#register_form')
    REG_EMAIL_INPUT = (By.NAME, 'registration-email')
    REG_PASS_INPUT = (By.NAME, 'registration-password1')
    REG_CONFIRM_PASS_INPUT = (By.NAME, 'registration-password2')
    REGISTER_NEW_USER_BUTTON_SUBMIT = (By.CSS_SELECTOR, "button[name=\"registration_submit\"]")


class ProductPageLocators:
    ADD_TO_BASKET_BTN = (By.CSS_SELECTOR, '.btn-add-to-basket')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main h1')
    NAME_IN_ALERT = (By.CSS_SELECTOR, '.alertinner strong')
    ALERT_SUCCESS = (By.CSS_SELECTOR, '.alert-success')