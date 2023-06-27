import requests

URL = "http://127.0.0.1:8000/Student_list/"
r = requests.get(url=URL)
print(r)

# Extract the response data as JSON
data = r.json()
print(data)
