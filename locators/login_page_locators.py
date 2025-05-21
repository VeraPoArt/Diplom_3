from selenium.webdriver.common.by import By


class LoginPageLocators:

    SEARCH_LOGIN_BUTTON = (By.XPATH, '//form[contains(@class, "Auth_form")]//button[text()="Войти"]')
    SEARCH_ERROR_INVALID_PASSWORD = (
        By.XPATH, '//div[contains(@class, "input__container")]//p[text()="Некорректный пароль"]')
    SEARCH_LOGIN_EMAIL_INPUT = (By.XPATH,
                                '//div[contains(@class, "Auth_login")]//div[contains(@class, "input__container")]//input[@type="text" and @name="name"]')
    SEARCH_LOGIN_PASSWORD_INPUT = (By.XPATH,
                                   '//div[contains(@class, "Auth_login")]//div[contains(@class, "input__container")]//input[@type="password" and @name="Пароль"]')
    SEARCH_PASSWORD_RECOVERY_LINK_VIA_LOGIN_PAGE = (By.XPATH,
                                                    '//a[contains(@class, "Auth_link") and text()="Восстановить пароль"]')
