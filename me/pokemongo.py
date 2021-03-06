#web : web crawler, pokemongo.inven.co.kr scrape

import requests
from bs4 import BeautifulSoup

content = []

def to_file(_list):
    print('Writing...')
    with open('pokemongo_inven.txt', 'w', encoding='utf-8') as f:
        for item in _list:
            f.write(str(item) + '\n')
    print('Writing done')

def pokemongo_inven_spider():
    url = 'http://pokemongo.inven.co.kr/dataninfo/pokemon/'
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, 'html.parser')
    for item in soup.findAll('a', {'class': 'pokemonicon'}):
        name = item.find('span', {'class': 'pokemonname'}).string
        href = 'http://pokemongo.inven.co.kr' + item.get('href')
        pokemongo_get_skill(href)

def pokemongo_get_skill(url):
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, 'html.parser')
    info = []
    for name in soup.findAll('h1', {'class': 'pokemongoDbCommonTitle'}):
        info.append(name.text)
    for item in soup.findAll('div', {'class': 'Recommended'}):
        for attack in item.findAll('tr', {'recomm-data': '1', 'row-data': '1'}):
            for skill in attack.findAll('img'):
                info.append(skill.text.strip())
        for defense in item.findAll('tr', {'recomm-data': '2', 'row-data': '1'}):
            for skill in defense.findAll('img'):
                info.append(skill.text.strip())
    #print(info)
    content.append(info)

pokemongo_inven_spider()
to_file(content)
#pokemongo_get_skill('http://pokemongo.inven.co.kr/dataninfo/pokemon/detail.php?code=3')
