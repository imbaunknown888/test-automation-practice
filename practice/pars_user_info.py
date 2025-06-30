import requests

response_get = requests.get("https://reqres.in/api/users?page=2")

data_json = {"email": "eve.holt@reqres.in", "password": "cityslicka"}

headers = {'x-api-key': 'reqres-free-v1'}
response_post = requests.post("https://reqres.in/api/login", json = data_json, headers = headers)

data_get = response_get.json()
data_post = response_post.json()

if response_get.status_code == 200:
    print(f"Заголовки GET-запроса: {response_get.headers}")
else:
    print(f"Заголовки выводятся только при статус коде: 200. В данном ответе статус код: {response_get.status_code}")
if response_post.status_code == 200:
    print(f"Заголовки POST-запроса: {response_post.headers}")
else:
    print(f"Заголовки выводятся только при статус коде: 200. В данном ответе статус код: {response_get.status_code}")

print(f"GET-Запрос. Статус код: {response_get.status_code}")
print(f"POST-Запрос. Статус код: {response_post.status_code}")

if data_post:
    res = data_post.get("token")
    print(f"TOKEN: {res}")
else:
    print("no token")

if "data" in data_get:
    for user in data_get["data"]:
        print("Фамилия:", user.get("last_name", "Фамилия отсутствует"))
else:
    print("Нет данных о пользователях в ответе.")

def create_user(email, password):
    data_json = {"email": email, "password": password}
    headers = {'x-api-key': 'reqres-free-v1'}
    response_post = requests.post("https://reqres.in/api/register", json=data_json, headers=headers)
    data_post = response_post.json()
    if response_post.status_code == 200:
        print(f'id: {data_post.get("id")}')
    else:
        print(f"Статуст код ответа: {response_post.status_code}")

create_user("eve.holt@reqres.in","pistol" )
