import requests
from bs4 import BeautifulSoup

def web_spider(url, max_pages):
    page = 1
    while page <= max_pages:
        url_temp = url + str(page)
        source_code = requests.get(url_temp)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, 'html.parser')
        for item in soup.findAll('a', {'class': 'user-name'}):
            name = item.string
            href = 'https://www.thenewboston.com/' + item.get('href')
            print(name)
            get_single_item_data(href)
        page += 1

def get_single_item_data(url):
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, 'html.parser')
    for item in soup.findAll('table', {'class': 'details-table'}):
        for items in item.findAll('a'):
            href = items.get('href')
            print('\t', href)

nb_url = 'https://www.thenewboston.com/search.php?type=1&sort=pop&page='

web_spider(nb_url, 2)
