import allure
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from locators.order_feed_page_locators import OrderFeedPageLocators


class OrderFeedPage(BasePage):

    @allure.step('Проверить заголовок страницы ленты заказов')
    def check_feed_title_text(self):
        try:
            # Добавляем явное ожидание загрузки страницы
            self.wait_for_page_load_complete()
            time.sleep(0.5)  # Небольшая пауза для стабильности
            
            # Пробуем найти заголовок
            title = self.get_text_from_element(OrderFeedPageLocators.SEARCH_FEED_TITLE_TEXT)
            return title
        except:
            # Если не удалось найти заголовок, пробуем обновить страницу
            self.driver.refresh()
            self.wait_for_page_load_complete()
            time.sleep(0.5)
            return self.get_text_from_element(OrderFeedPageLocators.SEARCH_FEED_TITLE_TEXT)

    @allure.step('Кликнуть на заказ для открытия модального окна с деталями заказа')
    def click_to_order(self):
        self.check_element_is_clickable(OrderFeedPageLocators.SEARCH_MADE_ORDER)
        self.click_to_element(OrderFeedPageLocators.SEARCH_MADE_ORDER)

    @allure.step('Проверить открытие модального окна с деталями заказа')
    def get_order_details_text(self):
        return self.get_text_from_element(OrderFeedPageLocators.SEARCH_ORDER_DETAILS_TEXT)

    @allure.step('Получить количество заказов за все время')
    def get_orders_count_all_time(self):
        self.element_is_displayed(OrderFeedPageLocators.SEARCH_COUNTER_OF_ALL_TIME_IN_FEED)
        all_element_text = self.get_text_from_element(OrderFeedPageLocators.SEARCH_COUNTER_OF_ALL_TIME_IN_FEED)
        return all_element_text

    @allure.step('Получить количество заказов за сегодня')
    def get_orders_count_today(self):
        self.scroll_into_view(OrderFeedPageLocators.SEARCH_COUNTER_FOR_TODAY_IN_FEED)
        self.element_is_displayed(OrderFeedPageLocators.SEARCH_COUNTER_FOR_TODAY_IN_FEED)
        today_element_text = self.get_text_from_element(OrderFeedPageLocators.SEARCH_COUNTER_FOR_TODAY_IN_FEED)
        return today_element_text

    @allure.step('Получить данные о заказах в работе')
    def get_orders_in_progress(self):
        max_wait_time = 60
        polling_interval = 2
        
        self.wait_for_page_load_complete()
        
        title = self.get_text_from_element(OrderFeedPageLocators.SEARCH_FEED_TITLE_TEXT)
        if title != "Лента заказов":
            return "0"
        
        start_time = time.time()
        
        while time.time() - start_time < max_wait_time:
            work_elements = self.driver.find_elements(*OrderFeedPageLocators.SEARCH_ORDER_IN_WORK)
            
            if work_elements and len(work_elements) > 0:
                order_id = work_elements[0].text
                if order_id and order_id != "Все текущие заказы готовы!":
                    return order_id
            
            self.driver.refresh()
            self.wait_for_page_load_complete()
            time.sleep(polling_interval)
        
        all_done_elements = self.driver.find_elements(*OrderFeedPageLocators.SEARCH_ORDERS_IN_WORK_DONE)
        if all_done_elements and len(all_done_elements) > 0 and all_done_elements[0].is_displayed():
            return "Все текущие заказы готовы!"
        
        return "0"

    @allure.step('Подождать, когда появится номер заказа в работе')
    def wait_for_order_id_in_progress(self):
        order_id = 'Все текущие заказы готовы!'
        while order_id == 'Все текущие заказы готовы!':
            order_id = self.get_text_from_element(OrderFeedPageLocators.SEARCH_ORDER_IN_WORK)
            self.wait_for_order_id_in_progress(OrderFeedPageLocators.SEARCH_ORDER_IN_WORK)
        return order_id

    @allure.step('Проверить наличие номера заказа в работе')
    def check_order_id_in_progress(self):
        element_text = self.get_text_from_element(OrderFeedPageLocators.SEARCH_ORDER_IN_WORK)
        return element_text

    @allure.step('Проверить наличие номера заказа в ленте')
    def check_order_id_in_feed(self):
        self.element_is_displayed(OrderFeedPageLocators.SEARCH_ORDER_ID_IN_FEED)
        element_text = self.get_text_from_element(OrderFeedPageLocators.SEARCH_ORDER_ID_IN_FEED)
        return element_text.lstrip('#')

    @allure.step('Быстро получить данные о заказах в работе без длительного ожидания')
    def get_orders_in_progress_fast(self):
        # Сначала ищем заказы в разделе "В работе"
        work_elements = self.driver.find_elements(By.XPATH, '//p[text()="В работе"]/following-sibling::ul/li')
        
        for element in work_elements:
            order_id = element.text.strip()
            if order_id.isdigit():
                return order_id
        
        # Если не нашли в разделе "В работе", ищем среди всех числовых элементов на странице
        all_numbers = self.driver.find_elements(By.XPATH, '//p[contains(@class, "text_type_digits-default")]')
        
        for element in all_numbers:
            order_id = element.text.strip().lstrip('#')
            if order_id.isdigit():
                return order_id
        
        # Если ничего не нашли, возвращаем "0"
        return "0"

    @allure.step('Дождаться обновления счетчика "Выполнено за все время"')
    def wait_for_orders_count_all_time_update(self, initial_count, max_wait_time=30, polling_interval=2):
        start_time = time.time()
        
        if not initial_count or not initial_count.isdigit():
            return None
        
        initial_value = int(initial_count)
        
        while time.time() - start_time < max_wait_time:
            self.driver.refresh()
            self.wait_for_page_load_complete()
            
            current_count = self.get_orders_count_all_time()
            
            if not current_count or not current_count.isdigit():
                time.sleep(polling_interval)
                continue
            
            current_value = int(current_count)
            
            if current_value > initial_value:
                return current_count
            
            time.sleep(polling_interval)
        
        return None

    @allure.step('Найти заказ по конкретному ID на странице ленты')
    def find_order_by_id(self, target_id):
        """Поиск заказа с конкретным ID в любом месте на странице ленты"""
        if not target_id or not target_id.isdigit():
            return False
        
        # Очищаем ID от ведущих нулей для сравнения
        target_id_stripped = target_id.lstrip('0')
        
        try:
            # Ищем любые числовые ID на странице
            all_numbers = self.driver.find_elements(By.XPATH, 
                '//p[contains(@class, "text_type_digits-default")]')
            
            for element in all_numbers:
                found_id = element.text.strip().lstrip('#')
                if found_id and found_id.isdigit():
                    # Сравниваем без ведущих нулей
                    if found_id.lstrip('0') == target_id_stripped:
                        return True
        except:
            pass
        
        return False
