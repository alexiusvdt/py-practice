# cmd where python to find PATH
# requests library installed to PATH

import requests
api_url = "https://jsonplaceholder.typicode.com/todos/1"
response = requests.get(api_url)
# calling json on the response object views data from the API
response.json()
response.status_code
response.headers["content type"]
# create todo & send post request
todo = {"userId": 1, "title": "Buy milk", "completed": False}
response = requests.post(api_url, json=todo)
response.json()

# create todo dictionary & send post request
import requests
import json
api_url = "https://jsonplaceholder.typicode.com/todos"
todo = {"userId": 1, "title": "Buy milk", "completed": False}
headers =  {"Content-Type":"application/json"}
response = requests.post(api_url, data=json.dumps(todo), headers=headers)
response.json()
#{'userId': 1, 'title': 'Buy milk', 'completed': False, 'id': 201}

response.status_code
#201
