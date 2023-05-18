
import requests as requests

# (1) Define an url that is the address you want to access
url = 'https://www.datacamp.com/cheat-sheet/sql-basics-cheat-sheet'

# (2) simulate a browser sending a request to the server
response = requests.get(url=url)

# (3) Get the source code of the page in the response content meaning of the content
print(type(response))
# <class 'requests.models.Response'>
print(response.text)

print(response.url)

print(response.content)
# b'<!DOCTYPE html>\n<html lang="en-US">\n<head>\n ......
print(response.status_code)

print(response.headers)

