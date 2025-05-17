import pytest
from selenium import webdriver
import requests
import urls
import data
from helpers import Generator


@pytest.fixture(params=[data.browser_chrome, data.browser_firefox])
def driver(request):
    if request.param == data.browser_chrome:
        data.DRIVER_NAME = data.browser_chrome
        driver = webdriver.Chrome()
    elif request.param == data.browser_firefox:
        data.DRIVER_NAME = data.browser_firefox
        driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(urls.BASE_URL)
    yield driver
    driver.quit()


@pytest.fixture()
def create_new_user_and_delete():
    if hasattr(data, 'TEST_USER_EMAIL') and hasattr(data, 'TEST_USER_PASSWORD'):
        email = data.TEST_USER_EMAIL
        password = data.TEST_USER_PASSWORD
    else:
        email = Generator.generate_random_email(5)
        password = Generator.generate_random_string(7)
    
    name = Generator.generate_random_string(7)

    payload = {
        "email": email,
        "password": password,
        "name": name
    }

    response = requests.post(urls.USER_REGISTER_ENDPOINT, json=payload)
    response_json = response.json()
    token = response_json.get('accessToken')
    yield email, password, token
    
    if token:
        try:
            headers = {'Authorization': token}
            requests.delete(urls.USER_DELETE_ENDPOINT, headers=headers)
        except Exception:
            pass


def pytest_configure(config):
    config.addinivalue_line(
        "markers", "smoke: маркер для дымовых тестов"
    )
    config.addinivalue_line(
        "markers", "functional: маркер для функциональных тестов"
    )
    config.addinivalue_line(
        "markers", "ui: маркер для тестов пользовательского интерфейса"
    )
    config.addinivalue_line(
        "markers", "security: маркер для тестов безопасности"
    )
