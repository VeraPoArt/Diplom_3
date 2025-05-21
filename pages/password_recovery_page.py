import allure
import time
from selenium.webdriver.common.action_chains import ActionChains

from helpers import Generator
from locators.password_recovery_locators import PasswordRecoveryLocators
from pages.base_page import BasePage
from data import TEST_USER_EMAIL, TEST_USER_PASSWORD


class PasswordRecoveryPage(BasePage):

    @allure.step('Ввести почту для восстановления пароля')
    def enter_email_to_recovery_password(self):
        self.check_element_is_clickable(PasswordRecoveryLocators.SEARCH_RECOVERY_EMAIL_INPUT_FOCUSED)
        self.click_to_element(PasswordRecoveryLocators.SEARCH_RECOVERY_EMAIL_INPUT_FOCUSED)
        self.add_text_to_element(PasswordRecoveryLocators.SEARCH_RECOVERY_EMAIL_INPUT_FOCUSED, TEST_USER_EMAIL)
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
        self.add_text_to_element(PasswordRecoveryLocators.SEARCH_RECOVERY_ENTER_NEW_PASSWORD_FOCUSED, TEST_USER_PASSWORD)

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
        try:
            element = self.find_element_with_wait(PasswordRecoveryLocators.SEARCH_ICON_PASSWORD_RECOVERY_MAKE_VISIBLE)
            self.scroll_into_view_js(element)
            time.sleep(0.5)
            self.wait_for_element_to_be_clickable(PasswordRecoveryLocators.SEARCH_ICON_PASSWORD_RECOVERY_MAKE_VISIBLE)
            actions = ActionChains(self.driver)
            actions.move_to_element(element).click().perform()
            time.sleep(0.5)
        except Exception as e:
            print(f"Ошибка при клике по иконке видимости пароля: {str(e)}")
