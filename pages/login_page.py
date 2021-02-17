from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, "Url do not have login word"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not present"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REG_FORM), "Registration form is not present"

    def register_new_user(self, email, password):
        email_input = self.browser.find_element(*LoginPageLocators.REG_EMAIL_INPUT)
        email_input.send_keys(email)
        password_input = self.browser.find_element(*LoginPageLocators.REG_PASS_INPUT)
        password_input.send_keys(password)
        repeat_password_input = self.browser.find_element(*LoginPageLocators.REG_CONFIRM_PASS_INPUT)
        repeat_password_input.send_keys(password)
        button_submit = self.browser.find_element(*LoginPageLocators.REGISTER_NEW_USER_BUTTON_SUBMIT)
        button_submit.click()

