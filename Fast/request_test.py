import requests

response = requests.get("http://localhost:8000/posts/3")

print(response.text)