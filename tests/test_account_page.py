import allure
import pytest
import time

import urls
from pages.account_page import AccountPage
from pages.main_page import MainPage
from pages.login_page import LoginPage


@allure.epic("Личный кабинет пользователя")
@allure.feature("Управление профилем")
class TestAccountPage:

    @allure.story("Навигация в личном кабинете")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description("Проверка возможности перехода в личный кабинет авторизованного пользователя")
    @allure.title("Авторизованный пользователь может перейти в личный кабинет")
    @pytest.mark.smoke
    def test_account_button_click(self, driver, create_new_user_and_delete):
        main_page = MainPage(driver)
        main_page.click_account_button()
        email, password, _ = create_new_user_and_delete
        login_page = LoginPage(driver)
        login_page.user_login(email, password)
        account_page = AccountPage(driver)
        account_page.close_browser_modal()
        main_page.click_account_button()
        expected_result = 'Выход'

        assert account_page.check_logout_button() == expected_result, \
            "Кнопка 'Выход' не отображается на странице личного кабинета"

    @allure.story("История заказов")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("Проверка возможности перехода в раздел истории заказов из личного кабинета")
    @allure.title("Пользователь может просматривать историю своих заказов")
    @pytest.mark.functional
    def test_orders_history_click(self, driver, create_new_user_and_delete):
        main_page = MainPage(driver)
        main_page.click_account_button()
        email, password, _ = create_new_user_and_delete
        login_page = LoginPage(driver)
        login_page.user_login(email, password)
        account_page = AccountPage(driver)
        account_page.close_browser_modal()
        main_page.click_account_button()
        account_page.get_order_history()
        expected_result = urls.ORDER_HISTORY_URL

        assert account_page.check_order_history_url() == expected_result, \
            "URL страницы истории заказов не соответствует ожидаемому"

    @allure.story("Выход из аккаунта")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("Проверка возможности выхода из аккаунта из личного кабинета")
    @allure.title("Пользователь может выйти из аккаунта через личный кабинет")
    @pytest.mark.security
    def test_logout_from_account(self, driver, create_new_user_and_delete):
        main_page = MainPage(driver)
        main_page.click_account_button()
        email, password, _ = create_new_user_and_delete
        login_page = LoginPage(driver)
        login_page.user_login(email, password)
        
        account_page = AccountPage(driver)
        account_page.close_browser_modal()
        
        main_page.wait_for_page_load_complete()
        
        main_page.click_account_button()
        
        account_page.close_all_modals()
        
        account_page.logout_from_account()
        
        expected_result = 'Войти'
        assert login_page.get_login_button_from_login_page() == expected_result, \
            "После выхода из аккаунта не отображается кнопка 'Войти'"
