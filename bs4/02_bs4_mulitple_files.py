import requests  # Importing the requests library to send HTTP requests
from bs4 import BeautifulSoup

# How To Get The HTML
root = 'https://subslikescript.com'
website =f'{root}/movies'
result = requests.get(website)
content = result.text
soup = BeautifulSoup(content, 'lxml')



