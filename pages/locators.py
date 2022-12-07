from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, '#login_link')
    BUTTON_TO_BASKET = (By.CSS_SELECTOR, '.btn.btn-default')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators:
    pass


class BasketPageLocators:
    BASKET_NULL = (By.CSS_SELECTOR, '#content_inner > p')
    FORMA_PRODUCTS_IN_BASKET = (By.CSS_SELECTOR, '.basket_summary')
    BUTTON_VIEW_BASKET = (By.CSS_SELECTOR, '.basket-mini.pull-right.hidden-xs > span > a')


class LoginPageLocators:
    BUTTON_OPEN_FORM = (By.CSS_SELECTOR, '#registration_link')
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    REGISTER_INPUT_EMAIL_ADDRESS = (By.CSS_SELECTOR, '#id_registration-email')
    REGISTER_INPUT_PASSWORD = (By.CSS_SELECTOR, '#id_registration-password1')
    REGISTER_INPUT_CONFIRM_PASSWORD = (By.CSS_SELECTOR, '#id_registration-password2')
    REGISTER_BUTTON = (By.CSS_SELECTOR, '#register_form > button')


class ProductPageLocators:
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, '.btn.btn-lg.btn-primary.btn-add-to-basket')
    NAME_BOOK = (By.CSS_SELECTOR, '.col-sm-6.product_main>h1')
    MESSAGES_VIN = (By.CSS_SELECTOR, '#messages > div:nth-child(1)>div>strong')
    PRICE_BOOK = (By.CSS_SELECTOR, 'div.col-sm-6.product_main>p.price_color')
    PRICE_BOOK_IN_BASKET = (By.CSS_SELECTOR, "div.alert.alert-safe.alert-noicon.alert-info.fade.in strong")
