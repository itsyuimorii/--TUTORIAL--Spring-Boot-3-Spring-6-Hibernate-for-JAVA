
import urllib
import urllib.request
url = 'http://www.google.com'
'''
The program will initiate an HTTP request and open the specified URL, which will return an object indicating the URL response.
'''
response = urllib.request.urlopen(url)

print(type(response))

# methods

content = response.read()

content = response.readline()

print(response.getcode())

print(response.geturl())

print(response.getheaders())

