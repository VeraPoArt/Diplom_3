import allure
import pytest
import time

from pages.account_page import AccountPage
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.order_feed_page import OrderFeedPage
from data import TEST_USER_EMAIL, TEST_USER_PASSWORD


@allure.epic("Основной функционал приложения")
@allure.feature("Навигация и управление заказами")
class TestMainPage:

    @allure.story("Навигация по сайту")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description("Проверка перехода в конструктор бургера с любой страницы")
    @allure.title("Пользователь может перейти в конструктор со страницы профиля")
    @pytest.mark.smoke
    def test_click_constructor_link(self, driver, create_new_user_and_delete):
        main_page = MainPage(driver)
        main_page.click_account_button()
        email, password, _ = create_new_user_and_delete
        login_page = LoginPage(driver)
        login_page.user_login(email, password)
        account_page = AccountPage(driver)
        account_page.close_browser_modal()
        main_page.click_account_button()
        main_page.click_constructor_link()
        expected_result = 'Соберите бургер'

        assert main_page.check_constructor_title() == expected_result, \
            "Заголовок страницы конструктора не соответствует ожидаемому"

    @allure.story("Навигация")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("Проверка перехода на страницу ленты заказов")
    @allure.title("Переход на страницу ленты заказов")
    @pytest.mark.ui
    def test_click_feed_link(self, driver):
        main_page = MainPage(driver)
        main_page.click_login_button()
        login_page = LoginPage(driver)
        login_page.user_login(TEST_USER_EMAIL, TEST_USER_PASSWORD)
        
        # Закрываем все модальные окна
        main_page.close_all_modals()
        time.sleep(0.5)
        
        # Переходим на страницу ленты заказов
        main_page.get_feed()
        
        # Проверяем, что мы на нужной странице
        order_feed_page = OrderFeedPage(driver)
        feed_title = order_feed_page.check_feed_title_text()
        assert feed_title == "Лента заказов", f"Ожидался заголовок 'Лента заказов', получен '{feed_title}'"

    @allure.story("Информация об ингредиентах")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Проверка открытия модального окна с информацией об ингредиенте")
    @allure.title("При клике на ингредиент открывается окно с детальной информацией")
    @pytest.mark.ui
    def test_ingredient_details_modal_opened(self, driver):
        main_page = MainPage(driver)
        main_page.get_ingredient_details()
        expected_result = 'Детали ингредиента'

        assert main_page.check_ingredient_title_text() == expected_result, \
            "Модальное окно с деталями ингредиента не отображается"

    @allure.story("Информация об ингредиентах")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Проверка закрытия модального окна с информацией об ингредиенте")
    @allure.title("Модальное окно с деталями ингредиента закрывается при клике на крестик")
    @pytest.mark.ui
    def test_ingredient_details_modal_closed(self, driver):
        main_page = MainPage(driver)
        main_page.get_ingredient_details()
        main_page.close_ingredient_details_modal()
        expected_result = 'Соусы'

        assert main_page.check_ingredient_details_modal_closed() == expected_result, \
            "Модальное окно с деталями ингредиента не закрылось после клика на крестик"

    @allure.story("Конструктор бургеров")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("Проверка увеличения счетчика ингредиентов при добавлении в корзину")
    @allure.title("Счетчик ингредиентов увеличивается при добавлении в корзину")
    @pytest.mark.functional
    def test_add_ingredient_to_basket_count_increased(self, driver):
        main_page = MainPage(driver)
        before_ingredient_added = main_page.check_count_before_ingredient_added()
        main_page.add_ingredient()
        after_ingredient_added = main_page.check_count_after_ingredient_added()

        assert int(after_ingredient_added) > int(before_ingredient_added), \
            "Счетчик ингредиентов не увеличился после добавления ингредиента в корзину"

    @allure.story("Оформление заказа")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description("Проверка возможности оформления заказа авторизованным пользователем")
    @allure.title("Авторизованный пользователь может оформить заказ")
    @pytest.mark.smoke
    def test_make_order_authorized(self, driver, create_new_user_and_delete):
        email, password, _ = create_new_user_and_delete
        main_page = MainPage(driver)
        main_page.click_login_button()
        login_page = LoginPage(driver)
        login_page.user_login(email, password)
        main_page.make_order()
        expected_result = 'идентификатор заказа'
        assert main_page.check_order_id_text() == expected_result, \
            "Информация об идентификаторе заказа не отображается после оформления"
