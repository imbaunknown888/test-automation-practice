import pytest

from src.api_steps.items_api_registration import create_user
from src.api_steps.items_api_delete_user import delete_user

from test_items.data.register_data_positive import REGISTER_DATA
from test_items.data.register_data_negative import REGISTER_DATA_WITHOUT_PASSWORD, REGISTER_DATA_WITH_EMPTY_EMAIL_PASSWORD, REGISTER_DATA_WITH_NEGATIVE_PASSWORD

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


@pytest.mark.parametrize(
    "user_data, expected_code",
    [
        # Пароль отсутствует
        (REGISTER_DATA_WITHOUT_PASSWORD, 400),

        # Неверный email
        (REGISTER_DATA_WITH_EMPTY_EMAIL_PASSWORD, 400),

        # Некорректный password
        (REGISTER_DATA_WITH_NEGATIVE_PASSWORD, 400),
    ]
)
def test_create_user_negative(user_data, expected_code):
    response = create_user(user_data, expected_code)
    print(response)

    assert 'error' in response