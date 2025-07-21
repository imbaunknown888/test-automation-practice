import requests

from utils.api_helpers import positive_case_200

BASE_URL = "https://reqres.in/api"
BASE_HEADERS = {"x-api-key": "reqres-free-v1"}

NEGATIVE_URL_FOR_LIST_USERS = f"{BASE_URL}/users?page=1"
NEGATIVE_URL_FOR_LIST_USERS2 = f"{BASE_URL}/users?page=3"

# Список пользователей

def list_users(expected_status_code: int):
    response = requests.get(f"{BASE_URL}/users?page=2", headers=BASE_HEADERS)
    if 200 <= expected_status_code < 400:
        response.raise_for_status()
    print(f"Статус код: {response.status_code}")
    positive_case_200(response, 200)
    return response.json()
