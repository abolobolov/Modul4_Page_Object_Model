import time

import pytest

from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):
    def all_product_page(self):
        self.should_not_be_success_message()
        self.button_add_to_basket()
        self.should_be_name_book()
        self.should_be_price_book()
        self.success_message_should_disappear()

    def button_add_to_basket(self):
        button_add_basket = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        button_add_basket.click()
        self.solve_quiz_and_get_code()

    def should_be_name_book(self):
        messages = self.browser.find_element(*ProductPageLocators.MESSAGES_VIN)
        assert self.is_element_present(*ProductPageLocators.MESSAGES_VIN)
        name_book = self.browser.find_element(*ProductPageLocators.NAME_BOOK)
        time.sleep(2)
        print(messages.text)
        print(name_book.text)

        assert messages.text == name_book.text, 'Название книги не совпадает с том что добавлена в корзину'

    def should_be_price_book(self):
        price_book = self.browser.find_element(*ProductPageLocators.PRICE_BOOK)
        price_book_in_basket = self.browser.find_element(*ProductPageLocators.PRICE_BOOK_IN_BASKET)
        print(price_book.text)
        print(price_book_in_basket.text)

        assert price_book.text == price_book_in_basket.text, 'Цена на странице и в корзине отличаются'

    def should_not_be_success_message(self):# показывает есть ли сообщение об успешном добавлении товара в корзину, пока товар не добавлен в корзину
        assert self.is_not_element_present(*ProductPageLocators.MESSAGES_VIN), \
            "Присутствует сообщение об успешном добавлении товара в корзину, но товар не добавлен в корзину"

    @pytest.mark.xfail
    def success_message_should_disappear(self):# ждет пока сообщение об успешном добавлении товара исчезнет
        assert self.is_disappeared(*ProductPageLocators.MESSAGES_VIN), "Сообщение об успешном добавлении товара в " \
                                                                       "корзину не исчезает ====> ЛОЖНООТРИЦАТЕЛЬНЫЙ ТЕСТ"