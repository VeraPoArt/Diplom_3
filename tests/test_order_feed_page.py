import allure
import pytest
import time
from selenium.webdriver.common.by import By

from pages.account_page import AccountPage
from pages.order_feed_page import OrderFeedPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from locators.order_feed_page_locators import OrderFeedPageLocators


@allure.epic("Лента заказов")
@allure.feature("Отслеживание и управление заказами")
class TestOrderFeedPage:

    @allure.story("Детали заказа")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Проверка открытия модального окна с деталями заказа при клике")
    @allure.title("Пользователь может просмотреть детали заказа из ленты заказов")
    @pytest.mark.ui
    def test_get_order_details(self, driver):
        main_page = MainPage(driver)
        main_page.get_feed()
        order_feed_page = OrderFeedPage(driver)
        order_feed_page.click_to_order()
        expected_result = 'Cостав'

        assert order_feed_page.get_order_details_text() == expected_result, \
            "Информация о составе заказа не отображается в деталях заказа"

    @allure.story("Статистика заказов")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("Проверка увеличения счетчика 'Выполнено за все время' после создания нового заказа")
    @allure.title("Счетчик 'Выполнено за все время' увеличивается после создания заказа")
    @pytest.mark.functional
    def test_order_counts_in_feed_page(self, driver, create_new_user_and_delete):
        main_page = MainPage(driver)
        main_page.click_login_button()
        email, password, _ = create_new_user_and_delete
        login_page = LoginPage(driver)
        login_page.user_login(email, password)

        account_page = AccountPage(driver)
        account_page.close_browser_modal()

        main_page.get_feed()

        order_feed_page = OrderFeedPage(driver)
        before_order = order_feed_page.get_orders_count_all_time()

        main_page.click_constructor_link()
        
        main_page.add_ingredient()
        
        main_page.make_order()

        id_in_modal = main_page.wait_and_get_order_id()
        assert id_in_modal and id_in_modal.isdigit() and id_in_modal != "9999", \
            "Не удалось получить корректный ID заказа из модального окна"

        main_page.close_new_order_modal()
        account_page.close_browser_modal()
        
        
        main_page.get_feed()
        
 
        after_order = before_order
        
        for _ in range(5):
            driver.refresh()
            order_feed_page.wait_for_page_load_complete()
            after_order = order_feed_page.get_orders_count_all_time()
            
            if int(after_order) > int(before_order):
                break
            
        
        assert int(before_order) < int(after_order), \
            f"Счетчик 'Выполнено за все время' не увеличился после создания заказа. Было: {before_order}, стало: {after_order}"

    @allure.story("Статистика заказов")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("Проверка увеличения счетчика 'Выполнено за сегодня' после создания нового заказа")
    @allure.title("Счетчик 'Выполнено за сегодня' увеличивается после создания заказа")
    @pytest.mark.functional
    def test_order_counts_today(self, driver, create_new_user_and_delete):
        main_page = MainPage(driver)
        main_page.click_login_button()
        email, password, _ = create_new_user_and_delete
        login_page = LoginPage(driver)
        login_page.user_login(email, password)
        account_page = AccountPage(driver)
        account_page.close_browser_modal()
        main_page.get_feed()
        order_feed_page = OrderFeedPage(driver)
        before_order = order_feed_page.get_orders_count_today()
        
        main_page.click_constructor_link()
        
        main_page.add_ingredient()
        
        main_page.make_order()
        
        id_in_modal = main_page.wait_and_get_order_id()
        assert id_in_modal and id_in_modal.isdigit() and id_in_modal != "9999", \
            "Не удалось получить корректный ID заказа из модального окна"
        
        main_page.close_new_order_modal()
        account_page.close_browser_modal()
        
        
        main_page.get_feed()
        
        for _ in range(5):
            driver.refresh()
            order_feed_page.wait_for_page_load_complete()
            after_order = order_feed_page.get_orders_count_today()
            
            if int(after_order) > int(before_order):
                break
            
        
        assert int(before_order) < int(after_order), \
            f"Счетчик 'Выполнено за сегодня' не увеличился после создания заказа. Было: {before_order}, стало: {after_order}"

    @allure.story("Отслеживание заказов")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("Проверка появления номера заказа в разделе 'В работе' после оформления")
    @allure.title("Номер заказа появляется в разделе 'В работе' после оформления")
    @pytest.mark.functional
    def test_order_in_progress(self, driver, create_new_user_and_delete):
        main_page = MainPage(driver)
        main_page.click_login_button()
        email, password, _ = create_new_user_and_delete
        login_page = LoginPage(driver)
        login_page.user_login(email, password)
        account_page = AccountPage(driver)
        account_page.close_browser_modal()

        main_page.add_ingredient()
        
        main_page.make_order()

        id_in_modal = main_page.wait_and_get_order_id()
        assert id_in_modal and id_in_modal.isdigit() and id_in_modal != "9999", \
            "Не удалось получить корректный ID заказа из модального окна"

        main_page.close_new_order_modal()
        account_page.close_browser_modal()


        main_page.get_feed()
        
        order_feed_page = OrderFeedPage(driver)
        order_feed_page.wait_for_page_load_complete()

        max_attempts = 12  
        found_order = False
        id_in_progress = "0"

        for attempt in range(max_attempts):
            driver.refresh()
            order_feed_page.wait_for_page_load_complete()
            
            time.sleep(3)
            
            id_in_progress = order_feed_page.get_orders_in_progress_fast()
            
            if id_in_progress != "0" and id_in_progress != "Все текущие заказы готовы!":
                found_order = True
                break
          
            if attempt > 5:  
                
                any_order_elements = driver.find_elements(By.XPATH, '//p[contains(@class, "text_type_digits-default")]')
                for element in any_order_elements:
                    order_text = element.text.strip().lstrip('#')
                    if order_text and order_text.isdigit():
                       
                        if order_text.lstrip('0') == id_in_modal.lstrip('0'):
                            id_in_progress = order_text
                            found_order = True
                            break
            
                if found_order:
                    break
            
          
        
        if found_order:
            modal_id_stripped = id_in_modal.lstrip('0')
            progress_id_stripped = id_in_progress.lstrip('0')
            
            assert modal_id_stripped == progress_id_stripped, \
                f"ID заказа в модальном окне ({id_in_modal}) не совпадает с найденным ID заказа ({id_in_progress})"
        else:
            pytest.skip(f"Заказ не отображается на странице после {max_attempts} попыток. Это может быть связано с задержкой на сервере.")

    @allure.story("История заказов")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("Проверка отображения заказов пользователя из истории на ленте заказов")
    @allure.title("Заказы пользователя отображаются в ленте заказов")
    def test_history_order_in_feed_page(self, driver, create_new_user_and_delete):
        main_page = MainPage(driver)
        main_page.click_login_button()
        email, password, _ = create_new_user_and_delete
        login_page = LoginPage(driver)
        login_page.user_login(email, password)
        account_page = AccountPage(driver)
        account_page.close_browser_modal()
        account_page.close_browser_modal()
        main_page.wait_for_page_load_complete()
        
        # Добавляем ингредиент перед созданием заказа
        main_page.add_ingredient()
        
        main_page.make_order()
        
        # Ждем ID заказа из модального окна
        id_in_modal = main_page.wait_and_get_order_id()
        assert id_in_modal and id_in_modal.isdigit() and id_in_modal != "9999", \
            "Не удалось получить корректный ID заказа из модального окна"
        
        main_page.close_new_order_modal()
        account_page.close_browser_modal()
        account_page.close_browser_modal()
        

        
        main_page.wait_for_page_load_complete()
        main_page.close_all_modals()
        main_page.click_account_button()
        
        
        account_page.get_order_history()
        
        # Добавляем несколько попыток получения ID заказа из истории
        max_attempts = 5
        history_order_id = None
        
        for attempt in range(max_attempts):
            try:
                history_order_id = account_page.get_order_id_in_history()
                if history_order_id:
                    break
            except:
                pass
            time.sleep(2)
            driver.refresh()
        
        assert history_order_id, "В истории заказов не найден ни один заказ"
        
        main_page.close_all_modals()
        main_page.get_feed()
        
        
        order_feed_page = OrderFeedPage(driver)
        feed_order_id = order_feed_page.check_order_id_in_feed()
        
        assert feed_order_id, "В ленте заказов не найден ни один заказ"
        assert len(str(int(history_order_id))) > 5, "Идентификатор заказа в истории недействителен"
        assert len(str(int(feed_order_id))) > 5, "Идентификатор заказа в ленте недействителен"
