import requests

endpoint = "http://localhost:8000/api/products/"

data = {
  'title': 'This field is done',
  'price': 32.99
}
get_restponse = requests.post(endpoint, json=data)
# print(get_restponse.text)
print(get_restponse.json())