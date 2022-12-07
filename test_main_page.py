import pytest
from selenium.webdriver.common.by import By

from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from pages.main_page import MainPage

link = "http://selenium1py.pythonanywhere.com/en-gb"

def go_to_login_page(browser):
    login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")  # registration_link
    login_link.click()


@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        page = LoginPage(browser,
                         link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        page = LoginPage(browser, link)
        page.open()
        page.should_be_login_link()


def test_visible_form(browser):
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_page()


@pytest.mark.basket
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = BasketPage(browser, link)
    page.open()
    page.perehod_in_basket()
    page.show_null_product_in_basket()
    page.should_null_basket_text()


@pytest.mark.xfail
def test_guest_cant_see_product_in_basket_opened_from_main_page_NEGATIVE(browser):  # тест является ложноотрицательным
    page = BasketPage(browser, link)
    page.open()
    page.perehod_in_basket()
    page.show_null_product_in_basket()
    page.should_null_basket_text()
    page.negative_proverka_basket_page()

