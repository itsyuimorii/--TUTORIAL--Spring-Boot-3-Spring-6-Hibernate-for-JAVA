
# Using urllib to get the source code for Baidu's homepage
import urllib.request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# get request
# Get the first page of Douban movies and save it


url = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=0&limit=20'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
}

request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')

# (3) Data download to local
# The open method uses the gbk encoding by default. If we want to save Chinese characters then we need to specify the encoding format as utf-8 in the open method.

# encoding = 'utf-8'
# fp = open('douban.json','w',encoding='utf-8')
# fp.write(content)

with open('douban2.json', 'w', encoding='utf-8') as fp:
    fp.write(content)
