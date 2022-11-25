import urllib3 

http = urllib3.PoolManager()

# response = http.request("GET", "https://www.google.com/")
# print(response.status) # Prints 200

#making rest cal to spring boot app
# response = http.request("GET", "http://localhost:8586/employees/GetAllEmployees")

# print(response.data.decode("utf-8"))

# response = http.request("GET", "http://localhost:8586/employees/GetAllEmployees")

# print(response.data.decode("utf-8"))

# response = http.request("GET",
#                         "http://jsonplaceholder.typicode.com/posts/", 
#                         fields={"id": "1"})
# print(response.data.decode("utf-8"))

# response = http.request("POST", "http://jsonplaceholder.typicode.com/posts", fields={"title": "Created Post", "body": "Lorem ipsum", "userId": 5})

# print(response.data.decode("utf-8"))

# for i in range(1, 5):
#     response = http.request("DELETE", "http://jsonplaceholder.typicode.com/posts", fields={"id": i})
#     print(response.data.decode("utf-8"))