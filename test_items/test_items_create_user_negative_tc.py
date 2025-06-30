import pytest

from api_steps.items_api_steps import create_user, delete_user, create_new_user
from test_items.data.create_user_data_positive import CREATE_USER_DATA
from test_items.data.create_user_data_negative import CREATE_USER_DATA_NEGATIVE, CREATE_USER_DATA_NEGATIVE2, CREATE_USER_DATA_NEGATIVE3, CREATE_USER_DATA_NEGATIVE4, CREATE_USER_DATA_NEGATIVE5

"""
    Тест проверяет POST-запрос к эндпоинту /register/.

    Проверяет:
    - Создание аккаунта новым пользователем.
    - Статус ответа 201 OK.
    - Сервер возвращает пользователю "id", "token".
    - После прохождения тестов удаляет созданный аккаунт.
"""

@pytest.fixture()
def create_n3w_user():
    user = create_user(CREATE_USER_DATA, 201)
    user_name = user['name']
    yield user
    try:
        delete_user(user_name)
    except Exception:
        pass


"""
    Тест проверяет POST-запрос к эндпоинту /users/.

    Проверяет:
    - Создание аккаунта для нового пользователя из админки.
    - Статус ответа 400 OK.
    - Корректность структуры и содержания тела ответа.
    - Значения у ключа "job" отсутствует.
    """

def test_create_new_user():

        create_us3r = create_new_user(CREATE_USER_DATA_NEGATIVE, 400)
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

        create_us3r = create_new_user(CREATE_USER_DATA_NEGATIVE2,400)
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

        create_us3r = create_new_user(CREATE_USER_DATA_NEGATIVE3, 400)
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

        create_us3r = create_new_user(CREATE_USER_DATA_NEGATIVE4, 400)
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

        create_us3r = create_new_user(CREATE_USER_DATA_NEGATIVE5, 400)
        assert 'id' in create_us3r
        assert 'createdAt' in create_us3r
