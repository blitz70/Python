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
        for item in soup.findAll('a', {'class':'user-name'}):
            name = item.string
            href = 'https://www.thenewboston.com/' + item.get('href')
            print(name)
            get_single_item_data(href)
        page += 1

def get_single_item_data(url):
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, 'html.parser')
    for item in soup.findAll('table', {'class':'details-table'}):
        for items in item.findAll('a'):
            href = items.get('href')
            print('\t', href)

def pokemongo_inven_spider():
    url = 'http://pokemongo.inven.co.kr/dataninfo/pokemon/'
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, 'html.parser')
    for item in soup.findAll('a', {'class':'pokemonicon'}):
        name = item.find('span', {'class':'pokemonname'}).string
        href = 'http://pokemongo.inven.co.kr' + item.get('href')
        #print(name, href)
        pokemongo_get_skill_data(href)

def pokemongo_get_skill_data(url):
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, 'html.parser')
    for item in soup.findAll('div',{'class':'Recommended'}):
        skill = item.findAll('tr',{'row-data':'1'})
        print(skill)
        '''for items in item.findAll('a'):
            href = items.get('href')
            print('\t', href)'''


#thenewboston_spider(my_url, 1)
#pokemongo_inven_spider()
pokemongo_get_skill_data('http://pokemongo.inven.co.kr/dataninfo/pokemon/detail.php?code=1')
