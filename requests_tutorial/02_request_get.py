# @Time: 2023-05-18 2:21 p.m.
# @Author： Itsyuimoriispace
# @File: request_get
# @Project: Web Scraping in Python BeautifulSoup, Selenium & Scrapy 2023

import requests

x = requests.get('https://w3schools.com/python/demopage.htm')

print(x.text)