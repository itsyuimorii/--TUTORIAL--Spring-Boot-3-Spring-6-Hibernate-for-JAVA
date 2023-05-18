# _*_ coding: utf-8 
# @Time: 2023-05-18 1:24 p.m. 
# @Author： Itsyuimoriispace
# @File: urllib_methods
# @Project: Web Scraping in Python BeautifulSoup, Selenium & Scrapy 2023
import urllib.request

url = "http://www.google.com"

# (2) simulate a browser sending a request to the server
response = urllib.request.urlopen(url)

print(type(response))
#<class 'http.client.HTTPResponse'>


# method 1: read byte by byte
content = response.read()
print(content)

