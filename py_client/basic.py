from turtle import end_poly
import requests

endpoint = "https://httpbin.org/status/200/"
endpoint = "https://httpbin.org/anything"

get_restponse = requests.get(endpoint, json={"query":"hello world"})
print(get_restponse.text)
print(get_restponse.json())