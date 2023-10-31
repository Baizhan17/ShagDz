# Реализовать программу с интерфейсом для загрузки 
# выбранного количества файлов из https://jsonplaceholder.typicode.com/posts
import requests
import json

response = requests.get('https://jsonplaceholder.typicode.com/posts')
response_json = json.loads(response.text)

amount=int(input("Enter amount:"))
    
x = [response_json[i] for i in range(amount)]
print(x)
