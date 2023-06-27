import requests
URL = "http://127.0.0.1:8000/Student_list/"
a= requests.get(url=URL)
print(a)
#Extract from response
data= a.json()
print(data)
#This is the appliation who is calling API