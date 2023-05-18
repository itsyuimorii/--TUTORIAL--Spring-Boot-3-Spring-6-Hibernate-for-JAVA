# _*_ coding: utf-8 
# @Time: 2023-05-18 1:21 p.m. 
# @Author： Itsyuimoriispace
# @File: 01_urllib_basic_usage
# @Project: Web Scraping in Python BeautifulSoup, Selenium & Scrapy 2023
import requests as requests
# Use urllib to get the source code for the Baidu homepage


# (1) Define an url that is the address you want to access
url = 'http://www.google.com'

# (2) simulate a browser sending a request to the server
response = requests.get(url=url)

# (3) Get the source code of the page in the response content meaning of the content


# (4) Print the data


