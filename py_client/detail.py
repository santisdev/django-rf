from turtle import end_poly
import requests

endpoint = "http://localhost:8000/api/products/2/"

get_restponse = requests.get(endpoint)
# print(get_restponse.text)
print(get_restponse.json())