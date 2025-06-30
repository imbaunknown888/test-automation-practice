import requests

BASE_URL = "https://reqres.in/api"
BASE_HEADERS = {"x-api-key": "reqres-free-v1"}

NEGATIVE_URL_FOR_LIST_USERS = f"{BASE_URL}/users?page=1"
NEGATIVE_URL_FOR_LIST_USERS2 = f"{BASE_URL}/users?page=3"

# Создание нового аккаунта, Регистрация

def create_user(data, expected_status_code: int):
    response = requests.post(f"{BASE_URL}/register/", json=data, headers=BASE_HEADERS)
    if 200 <= expected_status_code < 400:
        response.raise_for_status()
    print(f"Статус код: {response.status_code}")
    return response.json()

# Удаление аккаунта пользователя

def delete_user(user_id):
    print(f"Trying to delete user with id={user_id}")
    try:
        response = requests.delete(f"{BASE_URL}users/{user_id}")
        return response.status_code
    except Exception as e:
        print("Error deleting user:", e)
        return None

# Авторизация пользователя

def login_user(data, expected_status_code: int):
    response = requests.post(f"{BASE_URL}/login/",json=data, headers=BASE_HEADERS)
    if 200 <= expected_status_code < 400:
        response.raise_for_status()
    print(f"Статус код: {response.status_code}")
    return response.json()

# Создание нового пользователя из админки

def create_new_user(data, expected_status_code: int):
    response = requests.post(f"{BASE_URL}/users/", json=data, headers=BASE_HEADERS)
    if 200 <= expected_status_code < 400:
        response.raise_for_status()
    print(f"Статус код: {response.status_code}")
    return response.json()

# Список пользователей

def list_users(expected_status_code: int):
    response = requests.get(f"{BASE_URL}/users?page=2", headers=BASE_HEADERS)
    if 200 <= expected_status_code < 400:
        response.raise_for_status()
    print(f"Статус код: {response.status_code}")
    return response.json()['data']
