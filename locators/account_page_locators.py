from selenium.webdriver.common.by import By


class AccountPageLocators:

    SEARCH_LOGOUT_BUTTON = (By.XPATH, '//button[contains(@class, "Account_button__") and text()="Выход"]')
    SEARCH_ORDERS_HISTORY = (By.XPATH, '//li[contains(@class, "Account_listItem")]/a[contains(@class, "Account_link") and contains(text(), "История заказов")]')
    SEARCH_MODAL_FF = (By.XPATH, '//div[contains(@class, "Modal_modal_overlay__")]')
    SEARCH_MODAL_CLOSE_FOR_FF = (By.XPATH, '//button[@class="close-modal-button"]')
    SEARCH_HEADER_ACCOUNT_PAGE = (By.XPATH, '//a[contains(@class, "AppHeader_header__link")]')
    SEARCH_ORDER_ID_IN_HISTORY = (By.XPATH, './/p[contains(@class, "text") and contains(@class, "text_type_digits-default")]')
