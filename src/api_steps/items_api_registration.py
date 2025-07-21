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
    assert response.status_code == expected_status_code, \
        f"Expected {expected_status_code}, got {response.status_code}"
    return response.json()