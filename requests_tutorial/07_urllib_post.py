import ssl
import urllib.request
import urllib.parse
import json

ssl._create_default_https_context = ssl._create_unverified_context


url = 'https://translate.google.com/'

headers = {
'User-Agent':
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
}

data = {
    'hl': 'python'
}

# post リクエストパラメータはエンコードする必要があります
data = urllib.parse.urlencode(data).encode('utf-8')

# post request parameters need to be placed in the custom parameters of the request object, not appended after the url
# post request parameters need to be encoded
request = urllib.request.Request(url=url, data=data, headers=headers)

# ブラウザがサーバーにリクエストを送信する様子をシミュレートします。
response = urllib.request.urlopen(request)

# Get the response data
content = response.read().decode('utf-8')

# String --> json object
obj = json.loads(content)
print(obj)

# The parameters of the post request method must be encoded data = urllib.parse.urlencode(data)
# After encoding, the encode method must be called data = urllib.parse.urlencode(data).encode('utf-8')
# The parameters are placed in the request object's custom method request = urllib.request.Request(url=url,data=data,headers=headers)
