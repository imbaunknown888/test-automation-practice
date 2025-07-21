import pytest

from src.api_steps.items_api_autorisation_user import login_user
from src.api_steps.items_api_registration import create_user
from src.api_steps.items_api_delete_user import delete_user

from test_items.data.register_data_positive import REGISTER_DATA
from test_items.data.login_data_positive import LOGIN_DATA
from test_items.data.login_data_negative import LOGIN_DATA_WITHOUT_PASSWORD, LOGIN_DATA_EMPTY_JSON


"""
    Тест проверяет POST-запрос к эндпоинту /register/.

    Проверяет:
    - Создание аккаунта новым пользователем.
    - Статус ответа 201 OK.
    - Сервер возвращает пользователю "id", "token".
    - После прохождения тестов удаляет созданный аккаунт.
"""

@pytest.fixture()
def test_create_user():
    user = create_user(REGISTER_DATA, 200)
    user_id = user['id']
    assert user['id'] in user
    assert user['email'] in user
    yield user
    try:
        delete_user(user_id)
    except Exception:
        pass

"""
    Тест проверяет POST-запрос к эндпоинту /login/.

    Проверяет:
    - Вход в аккаунт пользователя.
    - Статус ответа 200 OK.
    - Сервер возвращает "token".
"""

def test_login_user_positive():

    login_us3r = login_user(LOGIN_DATA, 200)
    assert 'token' in login_us3r

"""
    Тест проверяет POST-запрос к эндпоинту /login/.

    Проверяет:
    - Вход в аккаунт пользователя.
    - Отправка запроса без поля "password"
    - Статус ответа 400 OK.
    - Сервер возвращает "error" == 'Missing email or username'.
"""

def test_login_user_negative():

    login_us3r = login_user(LOGIN_DATA_WITHOUT_PASSWORD, 400)
    assert login_us3r['error'] == 'Missing password'

"""
    Тест проверяет POST-запрос к эндпоинту /login/.

    Проверяет:
    - Вход в аккаунт пользователя.
    - Отправка запроса без тела.
    - Статус ответа 400 OK.
    - Сервер возвращает "error" == 'Missing email or username'.
"""

def test_login_user_negative2():

    login_us3r = login_user(LOGIN_DATA_EMPTY_JSON, 400)
    assert login_us3r['error'] == 'Missing email or username'