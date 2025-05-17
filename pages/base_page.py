import allure
import time
from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

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
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(locator))
        self.find_element_with_wait(locator).click()

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
        action_chains = ActionChains(self.driver)
        action_chains.drag_and_drop(element, target).perform()

    @allure.step('Перетаскивание элемента с одного места на другое')
    def drag_and_drop_element(self, source_locator, target_locator):
        source_element = self.find_element_with_wait(source_locator)
        target_element = self.find_element_with_wait(target_locator)
        
        actions = ActionChains(self.driver)
        actions.drag_and_drop(source_element, target_element).perform()
        self.wait_for_page_load_complete(timeout=2)

    @allure.step('Клик по кнопке для скрытых модальных окон')
    def js_button_click(self, element):
        self.driver.execute_script("arguments[0].click();", element)
        
    @allure.step('Надежное закрытие всех модальных окон')
    def close_all_modals(self):
        overlay_elements = self.driver.find_elements(By.CSS_SELECTOR, "[class*='Modal_modal_overlay__']")
        
        for overlay in overlay_elements:
            if overlay.is_displayed():
                close_buttons = self.driver.find_elements(By.XPATH, 
                    '//button[contains(@class, "Modal_modal__close") or @class="close-modal-button"]')
                
                for button in close_buttons:
                    self.js_button_click(button)
                    time.sleep(0.3)
                    break

    @allure.step('Ожидание определенного URL')
    def wait_for_url_contains(self, url_part, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            expected_conditions.url_contains(url_part)
        )
        
    @allure.step('Ожидание стабильности DOM')
    def wait_for_page_load_complete(self, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            lambda d: d.execute_script('return document.readyState') == 'complete'
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