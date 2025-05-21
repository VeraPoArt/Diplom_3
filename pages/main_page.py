import allure
import time
import random
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
import data  # Возвращаем старый импорт


class MainPage(BasePage):

    @allure.step('Нажать на кнопку "Войти в аккаунт" на главной странице')
    def click_login_button(self):
        self.check_element_is_clickable(MainPageLocators.SEARCH_LOGIN_BUTTON_VIA_MAINPAGE)
        self.click_to_element(MainPageLocators.SEARCH_LOGIN_BUTTON_VIA_MAINPAGE)

    @allure.step('Нажать на ссылку "Личный кабинет" в хедере страницы')
    def get_account(self):
        self.close_all_modals()
        self.check_element_is_clickable(MainPageLocators.SEARCH_PERSONAL_ACCOUNT_LINK)
        account_button = self.find_element_with_wait(MainPageLocators.SEARCH_PERSONAL_ACCOUNT_LINK)
        self.js_button_click(account_button)

    @allure.step('Нажать на кнопку "Конструктор" в хедере')
    def click_constructor_link(self):
        self.check_element_is_clickable(MainPageLocators.SEARCH_CONSTRUCTOR)
        self.click_to_element(MainPageLocators.SEARCH_CONSTRUCTOR)

    @allure.step('Проверить заголовок конструктора')
    def check_constructor_title(self):
        return self.get_text_from_element(MainPageLocators.SEARCH_CONSTRUCTOR_TITLE_TEXT)

    @allure.step('Нажать на ссылку "Лента заказов" в хедере страницы')
    def get_feed(self):
        self.close_all_modals()
 #       time.sleep(0.5)  # Пауза после закрытия модальных окон
        
        # Находим и кликаем на ссылку ленты заказов
        feed_link = self.find_element_with_wait(MainPageLocators.SEARCH_FEED_VIA_MAIN_PAGE)
        self.scroll_into_view_js(feed_link)
 #       time.sleep(0.5)  # Пауза после скролла
        
        # Пробуем разные способы клика
        try:
            feed_link.click()
        except:
            try:
                self.js_button_click(feed_link)
            except:
                actions = ActionChains(self.driver)
                actions.move_to_element(feed_link).click().perform()
        
        # Ждем загрузки страницы и появления заголовка
        self.wait_for_page_load_complete()
  #      time.sleep(1)  # Дополнительная пауза для стабильности

    @allure.step('Нажать на ингредиент в конструкторе для просмотра деталей')
    def click_on_ingredient_details(self):
        self.check_element_is_clickable(MainPageLocators.SEARCH_INGREDIENT_DETAILS)
        self.click_to_element(MainPageLocators.SEARCH_INGREDIENT_DETAILS)

    @allure.step('Проверить заголовок ингредиента')
    def check_ingredient_title_text(self):
        return self.get_text_from_element(MainPageLocators.SEARCH_INGREDIENT_DETAILS_MODAL_TITLE)

    @allure.step('Закрыть модальное окно с деталями ингредиента')
    def close_ingredient_details_modal(self):
        self.check_element_is_clickable(MainPageLocators.SEARCH_INGREDIENT_DETAILS_MODAL_CLOSE)
        self.click_to_element(MainPageLocators.SEARCH_INGREDIENT_DETAILS_MODAL_CLOSE)

    @allure.step('Проверить закрытие модального окна с деталями ингредиента')
    def check_ingredient_details_modal_closed(self):
        return self.get_text_from_element(MainPageLocators.SEARCH_SAUCES_SECTION)

    @allure.step('Проверить текст вкладки "Соусы"')
    def check_sauces_section_text(self):
        return self.get_text_from_element(MainPageLocators.SEARCH_SAUCES_SECTION)

    @allure.step('Проверить значение счетчика ингредиентов до добавления')
    def check_counter_ingredient_not_added(self):
        return self.get_text_from_element(MainPageLocators.SEARCH_COUNTER_INGREDIENT_NOT_ADDED)

    @allure.step('Добавить ингредиент в заказ')
    def add_ingredient(self):
        # Закрываем все модальные окна перед началом
        self.close_all_modals()
        self.wait_for_page_load_complete()
        time.sleep(1)  # Пауза для стабилизации
        
        # Находим и кликаем на секцию булок
        buns_element = self.find_element_with_wait(MainPageLocators.SEARCH_BUNS_SECTION)
        self.scroll_into_view_js(buns_element)
        time.sleep(0.5)  # Пауза после скролла
        self.js_button_click(buns_element)
        time.sleep(0.5)  # Пауза после клика
        
        # Проверяем, что элементы кликабельны перед взаимодействием
        self.check_element_is_clickable(MainPageLocators.SEARCH_FIRST_BUN_IN_CONSTRUCTOR)
        self.check_element_is_clickable(MainPageLocators.SEARCH_TARGET_BASKET)
        
        # Находим элементы
        source = self.find_element_with_wait(MainPageLocators.SEARCH_FIRST_BUN_IN_CONSTRUCTOR)
        target = self.find_element_with_wait(MainPageLocators.SEARCH_TARGET_BASKET)
        
        # Скроллим к обоим элементам
        self.scroll_into_view_js(source)
        time.sleep(0.5)  # Пауза после скролла
        self.scroll_into_view_js(target)
        time.sleep(0.5)  # Пауза после скролла
        
        # Используем JavaScript для drag and drop независимо от браузера
        self.driver.execute_script("""
            function simulateDragDrop(sourceNode, destinationNode) {
                var EVENT_TYPES = {
                    DRAG_START: 'dragstart',
                    DRAG_ENTER: 'dragenter',
                    DRAG_OVER: 'dragover',
                    DROP: 'drop',
                    DRAG_END: 'dragend'
                }
                
                function createCustomEvent(type) {
                    var event = new DragEvent(type, {
                        bubbles: true,
                        cancelable: true,
                        dataTransfer: new DataTransfer()
                    });
                    return event;
                }
                
                sourceNode.dispatchEvent(createCustomEvent(EVENT_TYPES.DRAG_START));
                destinationNode.dispatchEvent(createCustomEvent(EVENT_TYPES.DRAG_ENTER));
                destinationNode.dispatchEvent(createCustomEvent(EVENT_TYPES.DRAG_OVER));
                destinationNode.dispatchEvent(createCustomEvent(EVENT_TYPES.DROP));
                sourceNode.dispatchEvent(createCustomEvent(EVENT_TYPES.DRAG_END));
            }
            
            simulateDragDrop(arguments[0], arguments[1]);
        """, source, target)
        
        # Ждем завершения действия
        self.wait_for_page_load_complete(timeout=2)
        time.sleep(1)  # Дополнительная пауза для стабилизации

    @allure.step('Проверить значение счетчика ингредиентов после добавления')
    def check_counter_ingredient_added(self):
        return self.get_text_from_element(MainPageLocators.SEARCH_COUNTER_INGREDIENT_ADDED)

    @allure.step('Нажать на кнопку "Оформить заказ"')
    def make_order(self):
        self.check_element_is_clickable(MainPageLocators.SEARCH_MAKE_ORDER_BUTTON)
        self.click_to_element(MainPageLocators.SEARCH_MAKE_ORDER_BUTTON)

    @allure.step('Проверить текст "Идентификатор заказа" в модальном окне заказа')
    def check_order_id_text(self):
        return self.get_text_from_element(MainPageLocators.SEARCH_ORDER_ID_TEXT)

    @allure.step('Ожидать и получить номер заказа')
    def wait_and_get_order_id(self):
        max_wait_time = 10
        polling_interval = 0.5
        start_time = time.time()
        
        while time.time() - start_time < max_wait_time:
            try:
                self.wait_for_invisibility(MainPageLocators.SEARCH_FOR_INVISIBILITY_OF_9999_IN_ORDER_MODAL)
                time.sleep(0.5)  # Пауза после проверки невидимости
                order_id = self.get_text_from_element(MainPageLocators.SEARCH_ORDER_ID_IN_MODAL)
                if order_id and order_id != "9999":
                    return order_id
            except:
                pass
            
            time.sleep(polling_interval)
        
        return self.get_text_from_element(MainPageLocators.SEARCH_ORDER_ID_IN_MODAL) or "9999"

    @allure.step('Получить номер заказа из модального окна')
    def check_order_id(self):
        element_text = self.get_text_from_element(MainPageLocators.SEARCH_ORDER_ID_IN_MODAL)
        if element_text:
            return element_text
        else:
            return "9999"

    @allure.step('Закрыть модальное окно о созданном заказе')
    def close_new_order_modal(self):
        try:
            self.wait_for_page_load_complete()
            time.sleep(0.5)  # Возвращаем паузу для стабильности
            
            # Находим кнопку закрытия
            close_button = self.find_element_with_wait(MainPageLocators.SEARCH_CLOSE_MADE_ORDER_BUTTON)
            
            # Пробуем разные способы клика
            try:
                close_button.click()
            except:
                try:
                    self.js_button_click(close_button)
                except:
                    actions = ActionChains(self.driver)
                    actions.move_to_element(close_button).click().perform()
                
            time.sleep(0.5)  # Пауза после закрытия
        except Exception as e:
            print(f"Ошибка при закрытии модального окна заказа: {str(e)}")

    @allure.step('Проверить счетчик после добавления ингредиента')
    def check_count_after_ingredient_added(self):
        return self.get_text_from_element(MainPageLocators.SEARCH_COUNTER_INGREDIENT_ADDED)

    @allure.step('Нажать на кнопку личного кабинета')
    def click_account_button(self):
        self.close_all_modals()
        time.sleep(0.5)  # Пауза после закрытия модальных окон
        account_button = self.find_element_with_wait(MainPageLocators.SEARCH_PERSONAL_ACCOUNT_LINK)
        self.js_button_click(account_button)
        time.sleep(0.5)  # Пауза после клика

    @allure.step('Открыть детали ингредиента')
    def get_ingredient_details(self):
        self.check_element_is_clickable(MainPageLocators.SEARCH_INGREDIENT_DETAILS)
        self.click_to_element(MainPageLocators.SEARCH_INGREDIENT_DETAILS)

    @allure.step('Проверить счетчик до добавления ингредиента')
    def check_count_before_ingredient_added(self):
        return self.get_text_from_element(MainPageLocators.SEARCH_COUNTER_INGREDIENT_NOT_ADDED)

    @allure.step('Ожидание кликабельности элемента')
    def wait_for_element_to_be_clickable(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            expected_conditions.element_to_be_clickable(locator)
        )

    @allure.step('Ожидание изменения состояния элемента')
    def wait_for_element_state_change(self, element, timeout=5):
        initial_class = element.get_attribute('class')
        WebDriverWait(self.driver, timeout).until(
            lambda d: element.get_attribute('class') != initial_class
        )

    @allure.step('Проверить успешность добавления ингредиента')
    def check_ingredient_added(self):
        try:
            counter = self.find_element_with_wait(MainPageLocators.SEARCH_COUNTER_INGREDIENT_ADDED)
            return counter.is_displayed()
        except:
            return False
