
import urllib.request
from lxml import etree
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

url = 'https://www.winnipeg.ca/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
}
request = urllib.request.Request(url = url,headers = headers)
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
tree = etree.HTML(content)
result = tree.xpath('//input[@id="globalSearchInput"]/@aria-label')[0]
print(result)





