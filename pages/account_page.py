import allure
import time

import data
from locators.account_page_locators import AccountPageLocators
from pages.base_page import BasePage


class AccountPage(BasePage):

    @allure.step('Закрыть модальное окно во всех браузерах')
    def close_browser_modal(self):
        """
        Универсальный метод для закрытия модальных окон независимо от браузера.
        Инкапсулирует специфичную для разных браузеров логику.
        """
        try:
            # Проверяем наличие модального окна
            modal_elements = [
                AccountPageLocators.SEARCH_MODAL_FF,  # Firefox
                AccountPageLocators.SEARCH_MODAL_CHROME  # Chrome (если есть отдельный локатор)
            ]
            
            for modal_locator in modal_elements:
                try:
                    modal = self.driver.find_element(*modal_locator)
                    if modal.is_displayed():
                        # Ищем кнопку закрытия
                        close_buttons = [
                            AccountPageLocators.SEARCH_MODAL_CLOSE_FOR_FF,
                            AccountPageLocators.SEARCH_MODAL_CLOSE_BUTTON  # Общий локатор, если есть
                        ]
                        
                        for button_locator in close_buttons:
                            try:
                                close_button = self.driver.find_element(*button_locator)
                                if close_button.is_displayed():
                                    self.js_button_click(close_button)
                                    # Ждем закрытия модального окна
                                    self.wait_for_modal_closed(self.driver, modal_locator)
                                    return  # Успешно закрыли, выходим
                            except:
                                continue  # Пробуем следующую кнопку
                except:
                    continue  # Пробуем следующее модальное окно
                
            # Дополнительный метод для закрытия других типов модальных окон
            self.close_all_modals()
        except Exception as e:
            # Логируем ошибку, но продолжаем выполнение
            print(f"Ошибка при закрытии модального окна: {str(e)}")

    @allure.step('Проверить наличие кнопки "Выход"')
    def check_logout_button(self):
        return self.get_text_from_element(AccountPageLocators.SEARCH_LOGOUT_BUTTON)

    @allure.step('Перейти в раздел истории заказов пользователя')
    def get_order_history(self):
        self.close_browser_modal()
        self.wait_for_page_load_complete()
        self.check_element_is_clickable(AccountPageLocators.SEARCH_ORDERS_HISTORY)
        orders_history_link = self.find_element_with_wait(AccountPageLocators.SEARCH_ORDERS_HISTORY)
        self.js_button_click(orders_history_link)
        self.wait_for_url_contains("order-history")

    @allure.step('Выйти из аккаунта пользователя')
    def logout_from_account(self):
        self.close_browser_modal()
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
