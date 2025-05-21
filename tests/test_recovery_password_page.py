import allure
import pytest

from pages.password_recovery_page import PasswordRecoveryPage
from pages.main_page import MainPage
from pages.login_page import LoginPage


@allure.epic("Аутентификация и управление учетной записью")
@allure.feature("Восстановление пароля")
class TestPasswordRecoveryPage:

    @allure.story("Процесс восстановления пароля")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("Проверка возможности восстановления пароля через указание email")
    @allure.title("Пользователь может инициировать восстановление пароля и ввести email")
    @pytest.mark.security
    def test_password_recovery(self, driver):
        password_recovery_page = PasswordRecoveryPage(driver)
        main_page = MainPage(driver)
        main_page.click_login_button()
        login_page = LoginPage(driver)
        login_page.click_to_recovery_password_link()
        password_recovery_page.enter_email_to_recovery_password()
        expected_result = 'Пароль'

        assert password_recovery_page.check_password_recovery_field() == expected_result, \
            "Не отображается поле для ввода нового пароля после ввода email"

    @allure.story("Видимость пароля")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Проверка возможности сделать пароль видимым")
    @allure.title("Пользователь может включить видимость пароля при восстановлении")
    @pytest.mark.ui
    def test_password_is_visible(self, driver):
        password_recovery_page = PasswordRecoveryPage(driver)
        main_page = MainPage(driver)
        main_page.click_login_button()
        login_page = LoginPage(driver)
        login_page.click_to_recovery_password_link()
        password_recovery_page.enter_email_to_recovery_password()
        password_recovery_page.enter_new_password()
        password_recovery_page.click_password_make_visible_hidden()

        assert password_recovery_page.check_password_visible(), \
            "Пароль не стал видимым после нажатия на иконку видимости"

    @allure.story("Видимость пароля")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Проверка возможности скрыть пароль после его отображения")
    @allure.title("Пользователь может скрыть пароль после его отображения")
    @pytest.mark.ui
    def test_password_is_hidden(self, driver):
        password_recovery_page = PasswordRecoveryPage(driver)
        main_page = MainPage(driver)
        main_page.click_login_button()
        login_page = LoginPage(driver)
        login_page.click_to_recovery_password_link()
        password_recovery_page.enter_email_to_recovery_password()
        password_recovery_page.enter_new_password()
        password_recovery_page.click_password_make_visible_hidden()
        password_recovery_page.click_password_make_visible_hidden()

        assert password_recovery_page.check_password_hidden(), \
            "Пароль не скрылся после повторного нажатия на иконку видимости"
