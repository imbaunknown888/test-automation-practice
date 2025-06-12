import requests

response = requests.get("https://reqres.in/api/users?page=2")

data = response.json()

users = data.get('data', [])

total = len(data)

for user in users:
    print(f"Email: {user['email']}")

print("Имя первого пользователя:", data['data'][0]['first_name'])

print(total)

