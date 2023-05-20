import requests  # Importing the requests library to send HTTP requests
from bs4 import BeautifulSoup  # Importing the BeautifulSoup library for HTML parsing
# How To Get The HTML
website = 'https://subslikescript.com/movie/Titanic-120338'  # The URL of the website to fetch content from
result = requests.get(website)  # Sending a GET request to fetch the website's response
content = result.text  # Extracting the content from the response
soup = BeautifulSoup(content, 'lxml')  # Parsing the HTML content using BeautifulSoup with the lxml parser

# print(soup.prettify())  # prints the HTML of the website

# Locate the box that contains title and transcript
box = soup.find('article', class_='main-article')
# Locate title and transcript
title = box.find('h1').get_text()
transcript = box.find('div', class_='full-script').get_text(strip=True, separator=' ')

# Exporting data in a text file with the "title" name
with open(f'{title}.txt', 'w') as file:
    file.write(transcript)