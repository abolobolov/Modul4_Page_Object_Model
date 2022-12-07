from .base_page import BasePage
from pages.locators import LoginPageLocators
from pages.locators import BasePageLocators
import faker


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.click_to_button_Login_Or_Register()
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def click_to_button_Login_Or_Register(self):
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, 'Не корректный url адрес'
        assert True

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"
        assert True

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"
        assert True

    def register_new_user(self, email, password):  # self,
        f = faker.Faker()
        email = self.browser.find_element(*LoginPageLocators.REGISTER_INPUT_EMAIL_ADDRESS).send_keys(email)
        #email.self.browser
        password = self.browser.find_element(*LoginPageLocators.REGISTER_INPUT_PASSWORD).send_keys('AA12345678')
        #password.send_keys('AA12345678')
        confirm_password = self.browser.find_element(*LoginPageLocators.REGISTER_INPUT_CONFIRM_PASSWORD).send_keys('AA12345678')
        #confirm_password.send_keys('AA12345678')
        button_register = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        button_register.click()