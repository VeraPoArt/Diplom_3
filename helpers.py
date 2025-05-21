import random
import string
from data import DRIVER_NAME, browser_chrome, browser_firefox


class Generator:

    @staticmethod
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for _ in range(length))
        return random_string

    @staticmethod
    def generate_random_email(length=None):
        """Генерирует случайный email или возвращает тестовый email.
        Если параметр length задан, генерирует случайный email,
        иначе возвращает тестовый email."""
        if length:
            characters = string.digits
            digits = ''.join(random.choice(characters) for _ in range(length))
            return f"burger_test_{digits}@burgerhouse.ru"
        else:
            return DRIVER_NAME.TEST_USER_EMAIL

    @staticmethod
    def get_test_password():
        """Возвращает тестовый пароль"""
        return DRIVER_NAME.TEST_USER_PASSWORD