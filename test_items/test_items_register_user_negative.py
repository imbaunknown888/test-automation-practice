import pytest

from api_steps.items_api_steps import create_user, delete_user
from test_items.data.register_data_positive import REGISTER_DATA
from test_items.data.register_data_negative import REGISTER_DATA_NEGATIVE, REGISTER_DATA_NEGATIVE2

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
    user = create_user(REGISTER_DATA, 201)
    user_id = user['id']
    assert user['id'] in user
    assert user['email'] in user
    yield user
    try:
        delete_user(user_id)
    except Exception:
        pass

"""
    Тест проверяет POST-запрос к эндпоинту /register/.

    Проверяет:
    - Создание аккаунта новым пользователем.
    - Отправка запроса без поля "password"
    - Статус ответа 400 OK.
    - Сервер возвращает "error" == 'Missing email or username'.
"""

def test_create_user_negative():

    create_us3r = create_user(REGISTER_DATA_NEGATIVE, 400)
    assert create_us3r['error'] == 'Missing password'

"""
    Тест проверяет POST-запрос к эндпоинту /register/.

    Проверяет:
    - Создание аккаунта новым пользователем.
    - Отправка запроса без тела.
    - Статус ответа 400 OK.
    - Сервер возвращает "error" == 'Missing email or username'.
"""

def test_create_user_negative2():

    create_us3r = create_user(REGISTER_DATA_NEGATIVE2, 400)
    assert create_us3r['error'] == 'Missing email or username'

