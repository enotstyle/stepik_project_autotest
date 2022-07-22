from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-group a.btn.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, ".basket-items")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_INPUT = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD1_INPUT = (By.CSS_SELECTOR, "#id_registration-password1")
    PASSWORD2_INPUT = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "#register_form button")


class MainPageLocators:
    pass


class ProductPageLocators:
    BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    BOOK_NAME = (By.CSS_SELECTOR, ".breadcrumb .active")
    ADD_MESSAGE = (By.CSS_SELECTOR, "div.alertinner > strong")
    BOOK_PRICE = (By.CSS_SELECTOR, ".product_main p.price_color")
    PRICE_MESSAGE = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
