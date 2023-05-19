# @Time: 2023-05-18 10:00 p.m.
# @Author： Itsyuimoriispace
# @File: 01_urllib_basic.py
# @Project: Web Scraping in Python BeautifulSoup, Selenium & Scrapy 2023

import urllib
import urllib.request

# (1) Define an url that is the address you want to access
url = 'http://www.google.com'

# (2) Simulate a browser sending a request to the server
response = urllib.request.urlopen(url)

# (3) Get the source code of the page in the response content meaning of the content
# The read method returns binary data in byte form
# We want to convert the binary data to a string
# binary - "string decode('format of encoding')
content = response.read().decode('utf-8')

# (4) Print data
print(content)



