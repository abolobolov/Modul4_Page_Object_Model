import faker
import pytest

from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
urls = [f"{link}/?promo=offer{no}" for no in range(10)]
link_2 = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207//?promo=offer0"

@pytest.mark.need_review
@pytest.mark.parametrize('link', urls)
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.all_product_page()

@pytest.mark.message('link_2')
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link_2)
    page.open()
    page.button_add_to_basket()
    page.should_not_be_success_message()


@pytest.mark.message('link_2')
def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link_2)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.message('link_2')
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link_2)
    page.open()
    page.button_add_to_basket()
    page.success_message_should_disappear()


def test_guest_should_see_login_link_on_product_page(browser):
    link3 = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link3)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link4 = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-big-u_93/"
    page = ProductPage(browser, link4)
    page.open()
    page.go_to_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link5 = 'https://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/'
    page = BasketPage(browser, link5)
    page.open()
    page.perehod_in_basket()
    page.show_null_product_in_basket()
    page.should_null_basket_text()


@pytest.mark.xfail
def test_guest_cant_see_product_in_basket_opened_from_product_page_NEGATIVE(browser):
    link5 = 'https://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/'
    page = BasketPage(browser, link5)
    page.open()
    page.perehod_in_basket()
    page.show_null_product_in_basket()
    page.should_null_basket_text()
    page.negative_proverka_basket_page()


@pytest.mark.login_user
class TestUserAddToBasketFromProductPage:
    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, link_2)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.all_product_page()



    def test_message_disappeared_after_adding_product_to_basket(self, browser):
        page = ProductPage(browser, link_2)
        page.open()
        page.button_add_to_basket()
        page.success_message_should_disappear()




    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link3 = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"

        page = LoginPage(browser, link3)

        page.open()
        f = faker.Faker()
        email = f.email()

        password = 'AA12345678'
        confirm_password = 'AA12345678'
        page.register_new_user(email=email, password=password)
        page.should_be_authorized_user()
