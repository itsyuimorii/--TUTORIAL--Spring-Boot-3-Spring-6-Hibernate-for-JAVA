import requests  # Importing the requests library to send HTTP requests
from bs4 import BeautifulSoup  # Importing the BeautifulSoup library for HTML parsing
# How To Get The HTML
root = 'https://subslikescript.com'  # this is the homepage of the website
website = f'{root}/movies'
result = requests.get(website)  # Sending a GET request to fetch the website's response
content = result.text  # Extracting the content from the response
soup = BeautifulSoup(content, 'lxml')  # Parsing the HTML content using BeautifulSoup with the lxml parser
# Locate title and transcript
#print(soup.prettify())  # prints the HTML of the website
box = soup.find('article', class_='main-article')

# Store each link in "links" list (href doesn't consider root aka "homepage", so we have to concatenate it later)
links = []
for link in box.find_all('a', href=True):  # find_all returns a list
    links.append(link['href'])
#print(links)

for link in links:
    result = requests.get(f'{root}/{link}')  # structure --> https://subslikescript.com/movie/X-Men_2-290334
    content = result.text  # Extracting the content from the response
    soup = BeautifulSoup(content, 'lxml')  # Parsing the HTML content using BeautifulSoup with
    box = soup.find('article', class_='main-article')
    # Locate the box that contains title and transcript
    title = box.find('h1').get_text()
    transcript = box.find('div', class_='full-script').get_text(strip=True, separator=' ')

    # Exporting data in a text file with the "title" name
    with open(f'{title}.txt', 'w') as file:
        file.write(transcript)