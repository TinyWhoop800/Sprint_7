import random
import allure
import string


@allure.step("Генерация случайной строки длиной {length}")
def generate_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


@allure.step("Генерация уникального логина")
def generate_unique_login():
    return f"courier_{generate_random_string(10)}"


@allure.step("Генерация уникального пароля")
def generate_unique_password():
    return generate_random_string(10)

@allure.step("Генерация уникального имени")
def generate_unique_first_name():
    return generate_random_string(10)