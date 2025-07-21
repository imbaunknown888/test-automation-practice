import pytest

from src.api_steps.items_api_steps import create_user, delete_user, login_user, list_users
from tests.data.login_data_positive import LOGIN_DATA
from tests.data.create_user_data_positive import CREATE_USER_DATA


"""
    Тест проверяет POST-запрос к эндпоинту /register/.

    Проверяет:
    - Создание аккаунта новым пользователем.
    - Статус ответа 201 OK.
    - Сервер возвращает пользователю "id", "token".
    - После прохождения тестов удаляет созданный аккаунт.
"""

@pytest.fixture()
def create_new_user():
    user = create_user(CREATE_USER_DATA, 201)
    user_name = user['name']
    yield user
    try:
        delete_user(user_name)
    except Exception:
        pass

"""
    Тест проверяет POST-запрос к эндпоинту /login/.

    Проверяет:
    - Вход в аккаунт пользователя.
    - Статус ответа 200 OK.
    - Сервер возвращает "token".
"""

def test_login_user():
    login_us3r = login_user(LOGIN_DATA, 200)
    assert 'token' in login_us3r

"""
    Тест проверяет POST-запрос к эндпоинту /login/.

    Проверяет:
    - Статус ответа 400 OK.
    - Сервер возвращает список пользователей с 1-й страницы.
"""

def test_list_user_negative1():
    list_us3rs_negative = list_users(400)
    assert list_us3rs_negative['data']['page'] == 1

"""
    Тест проверяет POST-запрос к эндпоинту /login/.

    Проверяет:
    - Статус ответа 400 OK.
    - Сервер возвращает список пользователей с 3-й страницы.
"""

def test_list_user_negative2():
    list_us3rs_negative = list_users(400)
    assert list_us3rs_negative['data']['page'] == 3

