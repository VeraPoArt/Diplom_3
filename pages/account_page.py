import allure
import time

import data
from locators.account_page_locators import AccountPageLocators
from pages.base_page import BasePage


class AccountPage(BasePage):

    @allure.step('Закрыть скрытое модальное окно')
    def close_modal(self):
        try:
            self.find_element_with_wait(AccountPageLocators.SEARCH_MODAL_FF)
            if self.element_is_displayed(AccountPageLocators.SEARCH_MODAL_FF):
                close_button = self.find_element_with_wait(AccountPageLocators.SEARCH_MODAL_CLOSE_FOR_FF)
                self.click_to_element(close_button)
                self.wait_for_modal_closed(self.driver, AccountPageLocators.SEARCH_HEADER_ACCOUNT_PAGE)
        except Exception as e:
            pass

    @allure.step('Закрыть скрытое модальное окно в firefox')
    def close_modal_for_ff(self):
        if data.DRIVER_NAME == data.browser_firefox:
            self.close_modal()

    @allure.step('Закрыть модальное окно в chrome')
    def close_modal_for_chrome(self):
        if data.DRIVER_NAME == data.browser_chrome:
            self.close_modal()

    @allure.step('Проверить наличие кнопки "Выход"')
    def check_logout_button(self):
        return self.get_text_from_element(AccountPageLocators.SEARCH_LOGOUT_BUTTON)

    @allure.step('Перейти в раздел истории заказов пользователя')
    def get_order_history(self):
        self.close_all_modals()
        self.wait_for_page_load_complete()
        self.check_element_is_clickable(AccountPageLocators.SEARCH_ORDERS_HISTORY)
        orders_history_link = self.find_element_with_wait(AccountPageLocators.SEARCH_ORDERS_HISTORY)
        self.js_button_click(orders_history_link)
        self.wait_for_url_contains("order-history")

    @allure.step('Выйти из аккаунта пользователя')
    def logout_from_account(self):
        self.close_all_modals()
        time.sleep(1)
        self.check_element_is_clickable(AccountPageLocators.SEARCH_LOGOUT_BUTTON)
        logout_button = self.find_element_with_wait(AccountPageLocators.SEARCH_LOGOUT_BUTTON)
        self.js_button_click(logout_button)

    @allure.step('Проверить URL страницы истории заказов')
    def check_order_history_url(self):
        return self.get_current_url()

    @allure.step('Проверить URL страницы авторизации')
    def check_login_url(self):
        return self.get_current_url()

    @allure.step('Получить id заказа из истории заказов в профиле пользователя')
    def get_order_id_in_history(self):
        self.element_is_displayed(AccountPageLocators.SEARCH_ORDER_ID_IN_HISTORY)
        element_text = self.get_text_from_element(AccountPageLocators.SEARCH_ORDER_ID_IN_HISTORY)
        return element_text.lstrip('#')
