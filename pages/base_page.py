import allure
import time
from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

# Добавляем импорты локаторов
from locators.main_page_locators import MainPageLocators
from locators.account_page_locators import AccountPageLocators

class BasePage:

    @allure.step('Инициализация веб-драйвера')
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Поиск элемента')
    def find_element_with_wait(self, locator):
        return WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(locator)
        )

    @allure.step('Кликабельность элемента')
    def check_element_is_clickable(self, locator):
        return WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(locator)
        )

    @allure.step('Ожидание для закрытия скрытого мадального окна')
    def wait_for_modal_closed(self, driver, locator):
        wait = WebDriverWait(driver, 2)
        return wait.until(expected_conditions.invisibility_of_element_located(locator))

    @allure.step('Клик по элементу')
    def click_to_element(self, locator):
        """Клик по элементу с обработкой ошибок и повторными попытками"""
        try:
            # Проверяем, является ли locator уже WebElement
            if isinstance(locator, WebElement):
                element = locator
            else:
                element = self.find_element_with_wait(locator)
            
            self.scroll_into_view_js(element)
 #           time.sleep(0.5)  # Возвращаем небольшую паузу для стабильности
            
            try:
                element.click()
            except:
                try:
                    actions = ActionChains(self.driver)
                    actions.move_to_element(element).click().perform()
                except:
                    self.driver.execute_script("arguments[0].dispatchEvent(new MouseEvent('click', {'bubbles': true}));", element)
        except Exception as e:
            raise Exception(f"Не удалось кликнуть по элементу {locator}: {str(e)}")

    @allure.step('Добавление текста в элемент')
    def add_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    @allure.step('Получение текста из элемента')
    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text

    @allure.step('Скролл до элемента')
    def scroll_into_view_js(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    @allure.step('Ожидание исчезновения элемента из видимости')
    def wait_disappear_element(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.invisibility_of_element_located(locator))

    @allure.step('Скролл до нужного элемента')
    def scroll_into_view(self, locator):
        element = self.find_element_with_wait(locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

    @allure.step("Получение текущего URL")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Отображение эдемента')
    def element_is_displayed(self, locator):
        return self.find_element_with_wait(locator).is_displayed()

    @allure.step('Перетаскивание элемента с одного места на другое для Chrome')
    def move_the_element(self, locator_element, locator_target):
        element = self.find_element_with_wait(locator_element)
        target = self.find_element_with_wait(locator_target)
        
        # Скроллим к элементам
        self.scroll_into_view_js(element)
 #       time.sleep(0.5)
        self.scroll_into_view_js(target)
  #      time.sleep(0.5)
        
        # Используем JavaScript для drag and drop
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
        """, element, target)
        
        # Ждем завершения действия
 #       time.sleep(1)

    @allure.step('Перетаскивание элемента с одного места на другое')
    def drag_and_drop_element(self, source_locator, target_locator):
        source_element = self.find_element_with_wait(source_locator)
        target_element = self.find_element_with_wait(target_locator)
        
        # Скроллим к элементам
        self.scroll_into_view_js(source_element)
        self.scroll_into_view_js(target_element)
        
        # Используем JavaScript для drag and drop
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
        """, source_element, target_element)
        
        # Ждем завершения действия
        self.wait_for_page_load_complete(timeout=2)

    @allure.step('Клик по кнопке для скрытых модальных окон')
    def js_button_click(self, element):
        self.driver.execute_script("arguments[0].click();", element)
        
    @allure.step('Закрыть все модальные окна')
    def close_all_modals(self):
        """Закрыть все модальные окна"""
        try:
            # Закрываем модальное окно авторизации, если оно есть
            try:
                auth_modal = self.find_element_with_wait(AccountPageLocators.SEARCH_CLOSE_MODAL_BUTTON, timeout=1)
                if auth_modal:
                    self.js_button_click(auth_modal)
                    time.sleep(0.5)
            except:
                pass

            # Закрываем модальное окно заказа, если оно есть
            try:
                order_modal = self.find_element_with_wait(MainPageLocators.SEARCH_CLOSE_MODAL_BUTTON, timeout=1)
                if order_modal:
                    self.js_button_click(order_modal)
                    time.sleep(0.5)
            except:
                pass

            # Закрываем модальное окно браузера, если оно есть
            try:
                browser_modal = self.find_element_with_wait(MainPageLocators.SEARCH_BROWSER_MODAL, timeout=1)
                if browser_modal:
                    self.js_button_click(browser_modal)
  #                  time.sleep(0.5)
            except:
                pass

            # Дополнительная проверка на наличие модальных окон
            try:
                modals = self.driver.find_elements(By.CLASS_NAME, "Modal_modal__content__2Fq_")
                for modal in modals:
                    try:
                        close_button = modal.find_element(By.CLASS_NAME, "Modal_modal__close__2Fq_")
                        self.js_button_click(close_button)
    #                    time.sleep(0.5)
                    except:
                        pass
            except:
                pass

        except Exception as e:
            print(f"Ошибка при закрытии модальных окон: {str(e)}")

    @allure.step('Ожидание определенного URL')
    def wait_for_url_contains(self, url_part, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            expected_conditions.url_contains(url_part)
        )
        
    @allure.step('Ожидание стабильности DOM')
    def wait_for_page_load_complete(self, timeout=10):
        """Ожидание полной загрузки страницы"""
        WebDriverWait(self.driver, timeout).until(
            lambda d: d.execute_script('return document.readyState') == 'complete'
        )

    @allure.step('Ожидание стабильности элемента')
    def wait_for_element_stable(self, element, timeout=5):
        """Ожидание стабильности элемента (прекращение анимаций)"""
        initial_location = element.location
        initial_size = element.size
        
        def element_is_stable(driver):
            current_location = element.location
            current_size = element.size
            return (current_location == initial_location and 
                    current_size == initial_size)
        
        WebDriverWait(self.driver, timeout).until(element_is_stable)

    @allure.step('Ожидание завершения анимации')
    def wait_for_animation_complete(self, element, timeout=5):
        """Ожидание завершения CSS анимаций"""
        WebDriverWait(self.driver, timeout).until(
            lambda d: d.execute_script("""
                const element = arguments[0];
                const style = window.getComputedStyle(element);
                return style.animation === 'none' && style.transition === 'none';
            """, element)
        )
        
    @allure.step('Ожидание появления элемента в DOM')
    def wait_for_presence_of_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            expected_conditions.presence_of_element_located(locator)
        )
        
    @allure.step('Ожидание, пока элемент станет видимым')
    def wait_for_visibility_of_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            expected_conditions.visibility_of_element_located(locator)
        )
        
    @allure.step('Ожидание, пока элемент будет содержать текст')
    def wait_for_text_to_be_present_in_element(self, locator, text, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            expected_conditions.text_to_be_present_in_element(locator, text)
        )
        
    @allure.step('Ожидание, пока элемент исчезнет')
    def wait_for_invisibility(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            expected_conditions.invisibility_of_element_located(locator)
        )
        
    @allure.step('Ожидание изменения текста элемента')
    def wait_for_text_change(self, locator, old_text, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            lambda driver: driver.find_element(*locator).text != old_text
        )

    @allure.step('Ожидание определенное количество секунд')
    def wait_seconds(self, seconds):
        time.sleep(seconds)

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