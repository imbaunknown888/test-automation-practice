import pytest
import requests

from src.api_steps.items_api_steps import create_user, delete_user, login_user, create_new_user, list_users
from test_items.data.register_data_positive import REGISTER_DATA
from test_items.data.login_data_positive import LOGIN_DATA
from test_items.data.create_user_data_positive import CREATE_USER_DATA

"""
    Тест проверяет POST-запрос к эндпоинту /register/.

    Проверяет:
    - Создание аккаунта новым пользователем.
    - Статус ответа 201 OK.
    - Сервер возвращает пользователю "id", "token".
    - После прохождения тестов удаляет созданный аккаунт.
"""

@pytest.fixture()
def test_registration_user():
    user = create_user(REGISTER_DATA, 201)
    user_id = user['id']
    yield user
    try:
        delete_user(user_id)
    except Exception:
        pass

"""
    Тест проверяет POST-запрос к эндпоинту /register/.

    Проверяет:
    - Создание аккаунта новым пользователем.
    - Статус ответа 200 OK.
    - Сервер возвращает пользователю "token".
"""

def test_login_user():
    login_us3r = login_user(LOGIN_DATA, 200)
    assert 'token' in login_us3r

"""
    Тест проверяет POST-запрос к эндпоинту /users/.

    Проверяет:
    - Создание аккаунта для нового пользователя администратором.
    - Статус ответа 201 OK.
    - Сервер возвращает пользователю "name", "job", "id".
"""

def test_create_new_user():
    create_us3r = create_new_user(CREATE_USER_DATA, 201)
    assert 'name' in create_us3r
    assert 'job' in create_us3r
    assert 'id' in create_us3r

"""
    Тест проверяет GET-запрос к эндпоинту /users?page=2/.

    Проверяет:
    - Создание аккаунта для нового пользователя администратором.
    - Статус ответа 200 OK.
    - Сервер возвращает пользователю "id", "email", "last_name".
"""

def test_list_us3rs():
    users = list_users(200)
    for user in users:
        assert 'id' in user
        assert 'email' in user
        assert 'last_name' in user