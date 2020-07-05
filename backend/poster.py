import requests
requests.post("http://localhost:5000/todo", json={"text":"my first todo", "description":"my first todo"})