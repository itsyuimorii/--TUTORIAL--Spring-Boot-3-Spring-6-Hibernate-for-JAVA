import urllib.request
import urllib.parse
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

url = 'https://www.google.com/search?q=ip'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
}


request = urllib.request.Request(url = url,headers= headers)

# ブラウザからサーバーへのアクセスをシミュレートする
# response = urllib.request.urlopen(request)

proxies = {
    'http':'66.235.200.69'
}
# handler  build_opener  open
handler = urllib.request.ProxyHandler(proxies = proxies)
opener = urllib.request.build_opener(handler)
response = opener.open(request)

content = response.read().decode('utf-8')

with open('ip.html','w',encoding='utf-8')as fp:
    fp.write(content)