import requests

BASE_URL = "https://reqres.in/api"
BASE_HEADERS = {"x-api-key": "reqres-free-v1"}

# Удаление аккаунта пользователя

def delete_user(user_id):
    print(f"Trying to delete user with id={user_id}")
    try:
        response = requests.delete(f"{BASE_URL}users/{user_id}")
        return response.status_code
    except Exception as e:
        print("Error deleting user:", e)
        return None