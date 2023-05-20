
import urllib.request
from lxml import etree
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


def create_request(page):

    if(page == 1):
        url = 'https://stock.adobe.com/ca/search?filters%5Bcontent_type%3Aphoto%5D=1&filters%5Bcontent_type%3Aillustration%5D=1&filters%5Bcontent_type%3Azip_vector%5D=1&filters%5Bcontent_type%3Avideo%5D=1&filters%5Bcontent_type%3Atemplate%5D=1&filters%5Bcontent_type%3A3d%5D=1&filters%5Bcontent_type%3Aaudio%5D=0&filters%5Binclude_stock_enterprise%5D=0&filters%5Bis_editorial%5D=0&filters%5Bfree_collection%5D=0&filters%5Bcontent_type%3Aimage%5D=1&k=animal&order=relevance&safe_search=1&limit=100&search_page=1&load_type=page&search_type=pagination&get_facets=0'
    else:
        url = 'https://stock.adobe.com/ca/search?filters%5Bcontent_type%3Aphoto%5D=1&filters%5Bcontent_type%3Aillustration%5D=1&filters%5Bcontent_type%3Azip_vector%5D=1&filters%5Bcontent_type%3Avideo%5D=1&filters%5Bcontent_type%3Atemplate%5D=1&filters%5Bcontent_type%3A3d%5D=1&filters%5Bcontent_type%3Aaudio%5D=0&filters%5Binclude_stock_enterprise%5D=0&filters%5Bis_editorial%5D=0&filters%5Bfree_collection%5D=0&filters%5Bcontent_type%3Aimage%5D=1&k=animal&order=relevance&safe_search=1&limit=100&search_page=1&load_type=page&search_type=pagination&get_facets=0'+ str(page) + '.html'


    headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
    }
    request = urllib.request.Request(url=url, headers=headers)
    return request
def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read()
    return content

def down_load(content):
    # urllib.request.urlretrieve('imageadress''filename')
    tree = etree.HTML(content)
    name_list = tree.xpath('//div[@id="search-results"]//a/img/@alt')
    url_list = tree.xpath('//div[@id="search-results"]//a/img/@src')



if __name__ == '__main__':
    start_page = int(input('please enter start page'))
    end_page = int(input('please enter end page'))

    for page in range(start_page,end_page):
        # (1) Request object customization
        request = create_request(page)
        # (2) Getting the source code of the page
        content = get_content(request)
        # (3) Download
        down_load(content)


