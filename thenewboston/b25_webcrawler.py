import requests
from bs4 import BeautifulSoup

my_url = 'https://www.thenewboston.com/search.php?type=1&sort=pop&page='

def to_file(arg):
    print(arg)
    file = open('b25.txt', 'w', encoding='utf-8')
    file.write(str(arg))
    file.close()

def thenewboston_spider(url, max_pages):
    page = 1
    while page <= max_pages:
        url_temp = url + str(page)
        source_code = requests.get(url_temp)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, 'html.parser')
        for link in soup.findAll('a', {'class':'user-name'}):
            name = link.string
            href = 'https://www.thenewboston.com/' + link.get('href')
            print(name, href)
        page += 1

thenewboston_spider(my_url, 1)