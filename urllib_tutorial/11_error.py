
import urllib.request
import urllib.error
import ssl


ssl._create_default_https_context = ssl._create_unverified_context
url = 'https://www.rottentomatoes.com/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
}
try:
    request = urllib.request.Request(url = url, headers = headers)
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    print(content)
except urllib.error.URLError:
    print('error')