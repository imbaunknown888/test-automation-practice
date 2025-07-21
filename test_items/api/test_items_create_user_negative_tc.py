import pytest

from src.api_steps.items_api_registration import create_user
from src.api_steps.items_api_create_new_user_from_admin import create_new_user
from test_items.data.create_user_data_positive import CREATE_USER_DATA
from test_items.data.create_user_data_negative import CREATE_USER_DATA_EMPTY_VALUE_JOB, CREATE_USER_DATA_EMPTY_VALUE_NAME, CREATE_USER_DATA_NAME_JOB_INT_VALUE, CREATE_USER_DATA_EMPTY_VALUE_NAME_JOB, CREATE_USER_DATA_EMPTY_JSON

"""
    Тест проверяет POST-запрос к эндпоинту /register/.

    Проверяет:
    - Создание аккаунта новым пользователем.
    - Статус ответа 201 OK.
    - Сервер возвращает пользователю "id", "token".
    - После прохождения тестов удаляет созданный аккаунт.
"""

def create_n3w_user():
    user = create_user(CREATE_USER_DATA, 201)

    assert user['name'] == 'morpheus'
    assert user['job'] == 'leader'


"""
    Тест проверяет POST-запрос к эндпоинту /users/.

    Проверяет:
    - Создание аккаунта для нового пользователя из админки.
    - Статус ответа 400 OK.
    - Корректность структуры и содержания тела ответа.
    - Значения у ключа "job" отсутствует.
    """

def test_create_new_user():

        create_us3r = create_new_user(CREATE_USER_DATA_EMPTY_VALUE_JOB, 400)
        assert 'name' in create_us3r
        assert 'job' in create_us3r
        assert 'id' in create_us3r
        assert 'createdAt' in create_us3r

"""
    Тест проверяет POST-запрос к эндпоинту /users/.

    Проверяет:
    - Создание аккаунта для нового пользователя из админки.
    - Статус ответа 400 OK.
    - Корректность структуры и содержания тела ответа.
    - Значения у ключа "name" отсутствует
    """

def test_create_new_user2():

        create_us3r = create_new_user(CREATE_USER_DATA_EMPTY_VALUE_NAME,400)
        assert 'name' in create_us3r
        assert 'job' in create_us3r
        assert 'id' in create_us3r
        assert 'createdAt' in create_us3r

"""
    Тест проверяет POST-запрос к эндпоинту /users/.

    Проверяет:
    - Создание аккаунта для нового пользователя из админки.
    - Статус ответа 400 OK.
    - Корректность структуры и содержания тела ответа.
    - Значения у ключей "job", "name" имеют числовой тип
"""

def test_create_new_user3():

        create_us3r = create_new_user(CREATE_USER_DATA_NAME_JOB_INT_VALUE, 400)
        assert 'name' in create_us3r
        assert 'job' in create_us3r
        assert 'id' in create_us3r
        assert 'createdAt' in create_us3r

"""
    Тест проверяет POST-запрос к эндпоинту /users/.

    Проверяет:
    - Создание аккаунта для нового пользователя из админки.
    - Статус ответа 400 OK.
    - Корректность структуры и содержания тела ответа.
    - Значения у ключей "job", "name" отсутствуют
"""

def test_create_new_user4():

        create_us3r = create_new_user(CREATE_USER_DATA_EMPTY_VALUE_NAME_JOB, 400)
        assert 'name' in create_us3r
        assert 'job' in create_us3r
        assert 'id' in create_us3r
        assert 'createdAt' in create_us3r

"""
    Тест проверяет POST-запрос к эндпоинту /users/.

    Проверяет:
    - Создание аккаунта для нового пользователя из админки.
    - Статус ответа 400 OK.
    - Корректность структуры и содержания тела ответа.
    - Отправка пустого тела запроса.
"""

def test_create_new_user5():

        create_us3r = create_new_user(CREATE_USER_DATA_EMPTY_JSON, 400)
        assert 'id' in create_us3r
        assert 'createdAt' in create_us3r
