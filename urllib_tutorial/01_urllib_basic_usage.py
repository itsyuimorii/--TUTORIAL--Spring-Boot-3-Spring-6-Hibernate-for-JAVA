# _*_ coding: utf-8 
# @Time: 2023-05-18 1:21 p.m. 
# @Author： Itsyuimoriispace
# @File: 01_urllib_basic_usage
# @Project: Web Scraping in Python BeautifulSoup, Selenium & Scrapy 2023

# Use urllib to get the source code for the Baidu homepage
import urllib.request


# (1) Define an url that is the address you want to access
url = 'http://www.baidu.com'

# (2) simulate a browser sending a request to the server
response = urllib.request.urlopen(url)

# (3) Get the source code of the page in the response content meaning of the content
# The read method returns binary data in byte form
# We want to convert the binary data to a string
# binary - "string decode ('format of encoding')
content = response.read().decode('utf-8')

# (4) Print the data
print(content)

