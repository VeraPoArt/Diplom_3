from selenium.webdriver.common.by import By


class MainPageLocators:

    SEARCH_LOGIN_BUTTON_VIA_MAINPAGE = \
        (By.XPATH, '//section[2]//button[contains(text(), "Войти в аккаунт")]')
    SEARCH_PERSONAL_ACCOUNT_LINK = (
        By.XPATH, '//a[contains(@class, "AppHeader_header__link") and .//p[text()="Личный Кабинет"]]')

    SEARCH_ORDER_BUTTON = (By.XPATH,
                           '//div[contains(@class, "BurgerConstructor_basket__container")]//button[contains(text(), "Оформить заказ")]')
    SEARCH_SAUCES_SECTION = (By.XPATH,
                             '//div[contains(@class, "tab_tab")]//span[text()="Соусы"]')
    SEARCH_FIRST_SAUCE_IN_CONSTRUCTOR = (
        By.XPATH,
        '//div[contains(@class, "tab_tab") and contains(@class, "tab_tab_type_current")]//span[text()="Соусы"]/ancestor::section//a[contains(@class, "BurgerIngredient_ingredient")]//p[text()="Соус Spicy-X"]')
    SEARCH_BUNS_SECTION = (By.XPATH, '//div[contains(@class, "tab_tab")]//span[text()="Булки"]')
    SEARCH_FIRST_BUN_IN_CONSTRUCTOR = (By.XPATH, '//p[text()="Флюоресцентная булка R2-D3"]')
    SEARCH_FILLINGS_SECTION = (By.XPATH, '//div[contains(@class, "tab_tab")]//span[text()="Начинки"]')
    SEARCH_FIRST_FILLING_IN_CONSTRUCTOR = (By.XPATH,
                                           '//div[contains(@class, "tab_tab") and contains(@class, "tab_tab_type_current")]//span[text()="Начинки"]/ancestor::section//a[contains(@class, "BurgerIngredient_ingredient")]//p[text()="Мясо бессмертных моллюсков Protostomia"]')
    SEARCH_CONSTRUCTOR = (By.XPATH, '//a[contains(@class, "AppHeader_header__") and .//p[contains(text(), "Конструктор")]]')
    SEARCH_FEED_VIA_MAIN_PAGE = (By.XPATH, '//a[contains(@class, "AppHeader_header__link") and @href="/feed" and .//p[contains(text(), "Лента Заказов")]]')
    SEARCH_CONSTRUCTOR_TITLE_TEXT = (By.XPATH, '//h1[@class="text text_type_main-large mb-5 mt-10"]')
    SEARCH_INGREDIENT_DETAILS = (By.XPATH, '//a[contains(@class, "BurgerIngredient_ingredient__") and .//img[@alt="Флюоресцентная булка R2-D3"]]')
    SEARCH_INGREDIENT_DETAILS_MODAL_TITLE = (By.XPATH, '//h2[contains(@class, "Modal_modal__title_modified") and contains(@class, "Modal_modal__title") and contains(@class, "text_type_main-large")]')
    SEARCH_INGREDIENT_DETAILS_MODAL_CLOSE = (By.XPATH, '//button[@type="button" and contains(@class, "Modal_modal__close_modified") and contains(@class, "Modal_modal__close")]')
    SEARCH_COUNTER_INGREDIENT_ADDED = (By.XPATH, '//div[contains(@class, "counter_counter__") and contains(@class, "counter_default__")]/p[contains(@class, "counter_counter__num__") and text()="2"]')
    SEARCH_COUNTER_INGREDIENT_NOT_ADDED = (By.XPATH, '//div[contains(@class, "counter_counter__") and contains(@class, "counter_default__")]/p[contains(@class, "counter_counter__num__") and text()="0"]')
    SEARCH_TARGET_BASKET = (By.XPATH, '//span[@class="constructor-element__text" and text()="Перетяните булочку сюда (низ)"]')
    SEARCH_ORDER_ID_TEXT = (By.XPATH, '//p[contains(@class, "undefined") and contains(@class, "text") and contains(@class, "text_type_main-medium") and contains(@class, "mb-15") and text()="идентификатор заказа"]')
    SEARCH_MAKE_ORDER_BUTTON = (By.XPATH, '//button[contains(@class, "button_button__") and contains(@class, "button_button_type_primary__") and contains(@class, "button_button_size_large__") and text()="Оформить заказ"]')
    SEARCH_CLOSE_MADE_ORDER_BUTTON = (By.XPATH, '//button[contains(@class, "Modal_modal__close_modified") and contains(@class, "Modal_modal__close")]')
    SEARCH_FOR_INVISIBILITY_OF_9999_IN_ORDER_MODAL = (By.XPATH, '//h2[contains(@class, "Modal_modal__title") and text()="9999"]')
    SEARCH_ORDER_ID_IN_MODAL = (By.XPATH, './/h2[contains(@class, "Modal_modal__title_shadow")]')