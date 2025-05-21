import allure
import time

from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):

    @allure.step('Перейти на страницу восстановления пароля')
    def click_to_recovery_password_link(self):
        self.check_element_is_clickable(LoginPageLocators.SEARCH_PASSWORD_RECOVERY_LINK_VIA_LOGIN_PAGE)
        self.click_to_element(LoginPageLocators.SEARCH_PASSWORD_RECOVERY_LINK_VIA_LOGIN_PAGE)

    @allure.step('Ввести email в поле ввода')
    def enter_email(self, email):
        self.add_text_to_element(LoginPageLocators.SEARCH_LOGIN_EMAIL_INPUT, email)

    @allure.step('Ввести пароль в поле ввода')
    def enter_password(self, password):
        self.add_text_to_element(LoginPageLocators.SEARCH_LOGIN_PASSWORD_INPUT, password)

    @allure.step('Нажать на кнопку "Войти"')
    def click_login_button(self):
        self.check_element_is_clickable(LoginPageLocators.SEARCH_LOGIN_BUTTON)
        self.click_to_element(LoginPageLocators.SEARCH_LOGIN_BUTTON)

    @allure.step('Авторизация пользователя')
    def user_login(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()
    
    @allure.step('Получить текст кнопки логина')
    def get_login_button_from_login_page(self):
        return self.get_text_from_element(LoginPageLocators.SEARCH_LOGIN_BUTTON)
    
    @allure.step('Проверить наличие кнопки "Восстановить пароль"')
    def check_recovery_password_link(self):
        return self.get_text_from_element(LoginPageLocators.SEARCH_PASSWORD_RECOVERY_LINK_VIA_LOGIN_PAGE)