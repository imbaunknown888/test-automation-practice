import pytest

from api_steps.items_api_steps import create_user, delete_user, create_new_user


REGISTER_DATA = {
    "email": "eve.holt@reqres.in",
    "password": "pistol"
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
def test_registration_user():
    user = create_user(REGISTER_DATA)
    user_id = user['id']
    yield user
    try:
        delete_user(user_id)
    except Exception:
        pass

def test_create_new_user():
    create_us3r = create_new_user(CREATE_USER_DATA_NEGATIVE)
    assert 'name' in create_us3r
    assert 'job' in create_us3r
    assert 'id' in create_us3r
    assert 'createdAt' in create_us3r

def test_create_new_user2():
    create_us3r = create_new_user(CREATE_USER_DATA_NEGATIVE2)
    assert 'name' in create_us3r
    assert 'job' in create_us3r
    assert 'id' in create_us3r
    assert 'createdAt' in create_us3r

def test_create_new_user3():
    create_us3r = create_new_user(CREATE_USER_DATA_NEGATIVE3)
    assert 'name' in create_us3r
    assert 'job' in create_us3r
    assert 'id' in create_us3r
    assert 'createdAt' in create_us3r

def test_create_new_user4():
    create_us3r = create_new_user(CREATE_USER_DATA_NEGATIVE4)
    assert 'name' in create_us3r
    assert 'job' in create_us3r
    assert 'id' in create_us3r
    assert 'createdAt' in create_us3r

def test_create_new_user5():
    create_us3r = create_new_user(CREATE_USER_DATA_NEGATIVE5)
    assert 'name' in create_us3r
    assert 'job' in create_us3r
    assert 'id' in create_us3r
    assert 'createdAt' in create_us3r