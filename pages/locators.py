from selenium.webdriver.common.by import By

class MainPageLocators:
    pass

class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators:
    BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    BOOK_NAME = (By.CSS_SELECTOR, ".breadcrumb .active") #имя книги из навигации
    ADD_MESSAGE = (By.CSS_SELECTOR, "div.alertinner > strong") #высплывающее сообщение о добавление с именем книги
    BOOK_PRICE = (By.CSS_SELECTOR, ".product_main p.price_color") #стоимость книги из карточки товара
    PRICE_MESSAGE = (By.CSS_SELECTOR, ".alert-info .alertinner strong") #всплывающее сообщение со стоимостью книги

class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-group a.btn.btn-default")

class BasketPageLocators:
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, ".basket-items")