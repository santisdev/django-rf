from turtle import end_poly
import requests

# endpoint = "https://httpbin.org/status/200/"
endpoint = "http://localhost:8000/api/"

get_restponse = requests.post(endpoint, json={"title":"hello world2", "content":"hello world"})
# print(get_restponse.text)
print(get_restponse.json())