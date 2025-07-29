import requests

url = "http://127.0.0.1:8000/api/token/"  # your token endpoint

data = {
    "username": "guy",
    "password": "YwrqpF6M_:3:LvF"
}

response = requests.post(url, data=data)
print(response.status_code)
print(response.json())
