import requests

token = ""
url = ""
headers = {"Authorization": f"Bearer {token}"}
response = requests.get(url, headers=headers)
print(response)
