import pytest

from api_steps.items_api_steps import create_user, delete_user, login_user, list_users_negative


LOGIN_DATA = {
    "email": "eve.holt@reqres.in",
    "password": "cityslicka"
}

CREATE_USER_DATA_POSITIVE = {
    "name": "morpheus",
    "job": "leader"
}

@pytest.fixture()
def create_new_user():
    user = create_user(CREATE_USER_DATA_POSITIVE)
    user_name = user['name']
    yield user
    try:
        delete_user(user_name)
    except Exception:
        pass

def test_login_user():
    login_us3r = login_user(LOGIN_DATA)
    assert 'token' in login_us3r

def test_login_user_negative1():
    list_us3rs_negative = list_users_negative()
    list_us3rs_negative['data']['page'] = 1

def test_login_user_negative2():
    list_us3rs_negative = list_users_negative()
    list_us3rs_negative['data']['page'] = 3

