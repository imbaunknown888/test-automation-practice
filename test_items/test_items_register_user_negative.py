import pytest

from api_steps.items_api_steps import create_user, delete_user, create_user_negative


REGISTER_DATA_POSITIVE = {
    "email": "eve.holt@reqres.in",
    "password": "pistol"
}

REGISTER_DATA_NEGATIVE = {
"email": "sydney@fife"
}

REGISTER_DATA_NEGATIVE2 = {

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

def test_create_user_negative():

    create_us3r = create_user_negative(REGISTER_DATA_NEGATIVE)
    assert create_us3r['error'] == 'Missing password'

def test_create_user_negative2():

    create_us3r = create_user_negative(REGISTER_DATA_NEGATIVE2)
    assert create_us3r['error'] == 'Missing email or username'

