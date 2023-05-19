import ssl
import urllib.request
import urllib.parse
ssl._create_default_https_context = ssl._create_unverified_context

base_url = 'https://translate.google.com/'

headers = {
'User-Agent':
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
}