import pytest

from src.api_steps.items_api_registration import create_user
from src.api_steps.items_api_delete_user import delete_user
from src.api_steps.items_api_autorisation_user import login_user
from src.api_steps.items_api_list_users_negative import list_users

from test_items.data.login_data_positive import LOGIN_DATA
from test_items.data.create_user_data_positive import CREATE_USER_DATA

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
    list_us3rs_negative = list_users(200)
    assert list_us3rs_negative['total'] == 13

"""
    Тест проверяет POST-запрос к эндпоинту /login/.

    Проверяет:
    - Статус ответа 400 OK.
    - Сервер возвращает список пользователей с 3-й страницы.
"""

def test_list_user_negative2():
    list_us3rs_negative = list_users(200)
    assert list_us3rs_negative['page'] == 3

