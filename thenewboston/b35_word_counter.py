#web : web crawler 2, word count

import requests
from bs4 import BeautifulSoup

def start(url):
    word_list = []
    soup = BeautifulSoup(requests.get(url).text, 'html.parser')
    for text in soup.findAll('a', {'class': 'title text-semibold'}):
        words = text.string.split()
        for word in words:
            print(word)

start("https://thenewboston.com/forum/")