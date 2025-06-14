import requests

BASE_URL = "https://reqres.in/api"
BASE_HEADERS = {"x-api-key": "reqres-free-v1"}

NEGATIVE_URL_FOR_LIST_USERS = f"{BASE_URL}/users?page=1"
NEGATIVE_URL_FOR_LIST_USERS2 = f"{BASE_URL}/users?page=3"

def create_user(data):
    response = requests.post(f"{BASE_URL}/register/", json=data, headers=BASE_HEADERS)
    response.raise_for_status()
    assert response.status_code == 200
    print(f"Статус код: {response.status_code}")
    return response.json()

def create_user_negative(data):
    response = requests.post(f"{BASE_URL}/register/", json=data, headers=BASE_HEADERS)
    assert response.status_code == 400
    print(f"Статус код: {response.status_code}")
    return response.json()

def delete_user(user_id):
    print(f"Trying to delete user with id={user_id}")
    try:
        response = requests.delete(f"{BASE_URL}users/{user_id}")
        return response.status_code
    except Exception as e:
        print("Error deleting user:", e)
        return None

def login_user(data):
    response = requests.post(f"{BASE_URL}/login/",json=data, headers=BASE_HEADERS)
    response.raise_for_status()
    assert response.status_code == 200
    print(f"Статус код: {response.status_code}")
    return response.json()

def login_user_negative(data):
    response = requests.post(f"{BASE_URL}/login/",json=data, headers=BASE_HEADERS)
    assert response.status_code == 400
    print(f"Статус код: {response.status_code}")
    return response.json()

def create_new_user(data):
    response = requests.post(f"{BASE_URL}/users/", json=data, headers=BASE_HEADERS)
    response.raise_for_status()
    assert response.status_code == 201
    print(f"Статус код: {response.status_code}")
    return response.json()

def create_new_user_negative(data):
    response = requests.post(f"{BASE_URL}/users/", json=data, headers=BASE_HEADERS)
    response.raise_for_status()
    assert response.status_code == 201
    print(f"Статус код: {response.status_code}")
    return response.json()

def list_users():
    response = requests.get(f"{BASE_URL}/users?page=2", headers=BASE_HEADERS)
    response.raise_for_status()
    assert response.status_code == 200
    print(f"Статус код: {response.status_code}")
    return response.json()['data']

def list_users_negative():
    response = requests.get(f"{NEGATIVE_URL_FOR_LIST_USERS2}", headers=BASE_HEADERS)
    assert response.status_code == 200
    print(f"Статус код: {response.status_code}")
    return response.json()['data']

