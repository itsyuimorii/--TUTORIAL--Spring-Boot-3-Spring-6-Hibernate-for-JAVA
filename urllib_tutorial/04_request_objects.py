import urllib.request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

url = 'https://www.google.com'

headers = {
'User-Agent':
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
}

# Because the dictionary cannot be stored in the urlopen method, headers cannot be passed in
'''
Create a Request object to send an HTTP request. url is the destination URL to be requested and headers is a dictionary containing the headers to be added to the request. Here the request headers are passed through the headers parameter.
'''
request = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(request)
content = response.read()

print(content)
