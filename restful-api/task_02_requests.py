import requests

href= requests.get("https://jsonplaceholder.typicode.com/posts")

print(href.status_code)
print(href.json)
