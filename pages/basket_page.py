import time

from pages.base_page import BasePage
from pages.locators import BasketPageLocators


class BasketPage(BasePage):
    def show_null_product_in_basket(self):
        time.sleep(5)
        assert self.is_not_element_present(*BasketPageLocators.FORMA_PRODUCTS_IN_BASKET), \
            'В корзине присутствуют товары'

    def should_null_basket_text(self):
        basket_null = self.browser.find_element(*BasketPageLocators.BASKET_NULL)
        print(basket_null.text)
        assert basket_null.text, 'Корзина не пуста'

    def negative_proverka_basket_page(self):
        assert self.is_disappeared(
            *BasketPageLocators.BASKET_NULL), 'Тест прошел проверку, так как он негативный ====> ЛОЖНООТРИЦАТЕЛЬНЫЙ ТЕСТ'
