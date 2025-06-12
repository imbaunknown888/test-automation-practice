import pytest

from api_steps.items_api_steps import create_user, delete_user, create_new_user_negative


REGISTER_DATA = {
    "email": "eve.holt@reqres.in",
    "password": "pistol"
}

CREATE_USER_DATA_POSITIVE = {
    "name": "morpheus",
    "job": "leader"
}

CREATE_USER_DATA_NEGATIVE = {
    "name": "morpheus",
    "job": ""
}
CREATE_USER_DATA_NEGATIVE2 = {
    "name": "",
    "job": "leader"
}
CREATE_USER_DATA_NEGATIVE3 = {
    "name": 5,
    "job": 6
}
CREATE_USER_DATA_NEGATIVE4 = {
    "name": "",
    "job": ""
}
CREATE_USER_DATA_NEGATIVE5 = {

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

def test_create_new_user():

        create_us3r = create_new_user_negative(CREATE_USER_DATA_NEGATIVE)
        assert 'name' in create_us3r
        assert 'job' in create_us3r
        assert 'id' in create_us3r
        assert 'createdAt' in create_us3r


def test_create_new_user2():

        create_us3r = create_new_user_negative(CREATE_USER_DATA_NEGATIVE2)
        assert 'name' in create_us3r
        assert 'job' in create_us3r
        assert 'id' in create_us3r
        assert 'createdAt' in create_us3r


def test_create_new_user3():

        create_us3r = create_new_user_negative(CREATE_USER_DATA_NEGATIVE3)
        assert 'name' in create_us3r
        assert 'job' in create_us3r
        assert 'id' in create_us3r
        assert 'createdAt' in create_us3r


def test_create_new_user4():

        create_us3r = create_new_user_negative(CREATE_USER_DATA_NEGATIVE4)
        assert 'name' in create_us3r
        assert 'job' in create_us3r
        assert 'id' in create_us3r
        assert 'createdAt' in create_us3r


def test_create_new_user5():

        create_us3r = create_new_user_negative(CREATE_USER_DATA_NEGATIVE5)
        assert 'id' in create_us3r
        assert 'createdAt' in create_us3r
