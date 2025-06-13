import pytest

from api_steps.items_api_steps import create_user, delete_user, login_user, login_user_negative


REGISTER_DATA_POSITIVE = {
    "email": "eve.holt@reqres.in",
    "password": "pistol"
}

LOGIN_DATA_POSTIVE = {
    "email": "eve.holt@reqres.in",
    "password": "cityslicka"
}

LOGIN_DATA_NEGATIVE = {
    "email": "peter@klaven"
}

LOGIN_DATA_NEGATIVE2 = {

}

@pytest.fixture()
def test_create_user():
    user = create_user(REGISTER_DATA_POSITIVE)
    user_id = user['id']
    assert user['id'] in user
    assert user['email'] in user
    yield user
    try:
        delete_user(user_id)
    except Exception:
        pass

def test_login_user_positive():

    login_us3r = login_user(LOGIN_DATA_POSTIVE)
    assert 'token' in login_us3r

def test_login_user_negative():

    login_us3r = login_user_negative(LOGIN_DATA_NEGATIVE)
    assert login_us3r['error'] == 'Missing password'

def test_login_user_negative2():

    login_us3r = login_user_negative(LOGIN_DATA_NEGATIVE2)
    assert login_us3r['error'] == 'Missing email or username'