import ssl
import urllib.request
import urllib.parse
ssl._create_default_https_context = ssl._create_unverified_context


base_url = 'https://www.rottentomatoes.com/search?'

data = {
    'search': '愛してる',
    'actor': 'Keanu_Reeves'
}

new_data = urllib.parse.urlencode(data)
print(new_data)
# search=%E6%84%9B%E3%81%97%E3%81%A6%E3%82%8B&actor=Keanu_Reeves

headers = {
'User-Agent':
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
}

url = base_url + new_data
request = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(request)
content = response.read()
print(content)
