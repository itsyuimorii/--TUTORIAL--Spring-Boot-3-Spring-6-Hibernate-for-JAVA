import urllib
import urllib.request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

url = 'https://www.google.com'

headers = {
'User-Agent':
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
}

response = urllib.request.urlopen(url)

content = response.read()

print(content)
