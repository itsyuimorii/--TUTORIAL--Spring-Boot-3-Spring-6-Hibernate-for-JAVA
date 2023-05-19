import urllib.request
import ssl
import urllib.parse
ssl._create_default_https_context = ssl._create_unverified_context


url = 'https://www.rottentomatoes.com/search?search=action'

headers = {
'User-Agent':
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
}


name = urllib.parse.quote('action')
url = url + name

# Customizing the Request Object
request = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(url)
content = response.read()
# print(content)
print(name)