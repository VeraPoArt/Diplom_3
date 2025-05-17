from selenium.webdriver.common.by import By


class PasswordRecoveryLocators:

    SEARCH_EMAIL_INPUT_VIA_PASSWORD_RECOVERY = (By.XPATH,
    '//div[@class="input pr-6 pl-6 input_type_text input_size_default"]/input[@class="text input__textfield text_type_main-default"]')
    SEARCH_RECOVERY_PASSWORD_BUTTON = (By.XPATH,
    '//form[contains(@class, "Auth_form")]//button[contains(@class, "button_button") and contains(@class, "button_button_type_primary") and text()="Восстановить"]')
    SEARCH_RECOVERY_PASSWORD_INPUT = (
    By.XPATH, '//div[contains(@class, "input_type_password") and .//label[text()="Пароль"]]')
    SEARCH_RECOVERY_EMAIL_INPUT_FOCUSED = (By.XPATH, '//div[contains(@class, "input") and contains(@class, "input_type_text")]//input[@type="text" and @name="name"]')
    SEARCH_ICON_PASSWORD_RECOVERY_MAKE_VISIBLE = (By.XPATH, '//div[@class="input__icon input__icon-action"]/*[local-name() = "svg"]')
    SEARCH_RECOVERY_ENTER_NEW_PASSWORD_FOCUSED = (By.XPATH, '//div[contains(@class, "input_type_password")]//input[@type="password"]')
    PASSWORD_VISIBLE_FIELD_ACTIVE = (By.XPATH,  '//label[text()="Пароль"]/parent::div[contains(@class,''"input_status_active")]')
    PASSWORD_HIDE_FIELD_NOT_ACTIVE = (By.XPATH, '//label[text()="Пароль"]/parent::div[contains(@class,''"input_type_password")]')