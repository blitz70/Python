#web : web crawler 2, word count

import requests
from bs4 import BeautifulSoup
import operator

def extract_words(url):
    word_list = []
    source = requests.get(url).text
    soup = BeautifulSoup(source, 'html.parser')
    for text in soup.findAll('a', {'class': 'title text-semibold'}):
        words = text.string.split()
        for word in words:
            word_list.append(word)
    return word_list

def clean_up(word_list):
    clean_word_list = []
    symbols = "~`!@#$%^&*()_-+={[}]|\:;\"'<,>.?/"
    for word in word_list:
        for symbol in symbols:
            word = word.replace(symbol, '')
        if len(word) > 0:
            clean_word_list.append(word.lower())
    return clean_word_list

def count_words(word_list):
    word_count_dictionary = {}
    for word in word_list:
        if word in word_count_dictionary:
            word_count_dictionary[word] += 1
        else:
            word_count_dictionary[word] = 1
    '''for key, value in sorted(word_count_dictionary.items(), key=operator.itemgetter(1)):
        print(key, value)'''
    return word_count_dictionary

def analayze(url):
    extracted_list = extract_words(url)
    clean_list = clean_up(extracted_list)
    result = count_words(clean_list)
    [print(key, value) for key, value in sorted(result.items(), key=operator.itemgetter(1))]

url = "https://thenewboston.com/forum/"
analayze(url)