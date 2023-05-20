import urllib.request
import urllib.parse
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

url = 'https://www.google.com/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
}


# Create a request object with the specified URL and headers
request = urllib.request.Request(url=url, headers=headers)

# Create an HTTPHandler
handler = urllib.request.HTTPHandler()

# Create a custom opener object
opener = urllib.request.build_opener(handler)

# Send the request using the opener and get the response
response = opener.open(request)

# Read the response data and decode it using UTF-8 encoding
content = response.read().decode('utf-8')

# Print the response content
print(content)