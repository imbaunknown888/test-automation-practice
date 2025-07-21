import requests

BASE_URL = "https://reqres.in/api"
BASE_HEADERS = {"x-api-key": "reqres-free-v1"}

# Авторизация пользователя

def login_user(data, expected_status_code: int):
    response = requests.post(f"{BASE_URL}/login/",json=data, headers=BASE_HEADERS)
    if 200 <= expected_status_code < 400:
        response.raise_for_status()
    print(f"Статус код: {response.status_code}")
    return response.json()