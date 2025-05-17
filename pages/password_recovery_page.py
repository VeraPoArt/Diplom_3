import allure

from helpers import Generator
from locators.password_recovery_locators import PasswordRecoveryLocators
from pages.base_page import BasePage
import data



class PasswordRecoveryPage(BasePage):

    @allure.step('Ввести почту для восстановления пароля')
    def enter_email_to_recovery_password(self):
        self.check_element_is_clickable(PasswordRecoveryLocators.SEARCH_RECOVERY_EMAIL_INPUT_FOCUSED)
        self.click_to_element(PasswordRecoveryLocators.SEARCH_RECOVERY_EMAIL_INPUT_FOCUSED)
        self.add_text_to_element(PasswordRecoveryLocators.SEARCH_RECOVERY_EMAIL_INPUT_FOCUSED, data.TEST_USER_EMAIL)
        self.click_to_element(PasswordRecoveryLocators.SEARCH_RECOVERY_PASSWORD_BUTTON)

    @allure.step('Проверить поле ввода пароля')
    def check_password_input(self):
        return self.get_text_from_element(PasswordRecoveryLocators.SEARCH_RECOVERY_PASSWORD_INPUT)

    @allure.step('Нажать на иконку показа пароля')
    def click_on_show_password_icon(self):
        self.check_element_is_clickable(PasswordRecoveryLocators.SEARCH_ICON_PASSWORD_RECOVERY_MAKE_VISIBLE)
        self.click_to_element(PasswordRecoveryLocators.SEARCH_ICON_PASSWORD_RECOVERY_MAKE_VISIBLE)

    @allure.step('Ввести новый пароль')
    def enter_new_password(self):
        self.check_element_is_clickable(PasswordRecoveryLocators.SEARCH_RECOVERY_ENTER_NEW_PASSWORD_FOCUSED)
        self.click_to_element(PasswordRecoveryLocators.SEARCH_RECOVERY_ENTER_NEW_PASSWORD_FOCUSED)
        self.add_text_to_element(PasswordRecoveryLocators.SEARCH_RECOVERY_ENTER_NEW_PASSWORD_FOCUSED, data.TEST_USER_PASSWORD)

    @allure.step('Проверить, что пароль скрыт')
    def check_password_visible(self):
        return self.element_is_displayed(PasswordRecoveryLocators.PASSWORD_VISIBLE_FIELD_ACTIVE)

    @allure.step('Проверить, что пароль виден')
    def check_password_hidden(self):
        return self.element_is_displayed(PasswordRecoveryLocators.PASSWORD_HIDE_FIELD_NOT_ACTIVE)

    @allure.step('Проверить наличие поля восстановления пароля')
    def check_password_recovery_field(self):
        return self.get_text_from_element(PasswordRecoveryLocators.SEARCH_RECOVERY_PASSWORD_INPUT)

    @allure.step('Нажать на кнопку видимости/невидимости пароля')
    def click_password_make_visible_hidden(self):
        self.check_element_is_clickable(PasswordRecoveryLocators.SEARCH_ICON_PASSWORD_RECOVERY_MAKE_VISIBLE)
        self.click_to_element(PasswordRecoveryLocators.SEARCH_ICON_PASSWORD_RECOVERY_MAKE_VISIBLE)
