import pytest

from api_steps.items_api_steps import create_user, delete_user, login_user, create_new_user, list_users


REGISTER_DATA = {
    "email": "eve.holt@reqres.in",
    "password": "pistol"
}

LOGIN_DATA = {
    "email": "eve.holt@reqres.in",
    "password": "cityslicka"
}

CREATE_USER_DATA = {
    "name": "morpheus",
    "job": "leader"
}

@pytest.fixture()
def test_registration_user():
    user = create_user(REGISTER_DATA)
    user_id = user['id']
    yield user
    try:
        delete_user(user_id)
    except Exception:
        pass

def test_login_user():
    login_us3r = login_user(LOGIN_DATA)
    assert 'token' in login_us3r

def test_create_new_user():
    create_us3r = create_new_user(CREATE_USER_DATA)
    assert 'name' in create_us3r
    assert 'job' in create_us3r
    assert 'id' in create_us3r

def test_list_us3rs():
    users = list_users()
    for user in users:
        assert 'id' in user
        assert 'email' in user
        assert 'last_name' in user