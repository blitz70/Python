#web : download pics

import random as rd
import urllib.request as rq

def download_web_image(url):
    no = rd.randrange(1,1000)
    file_name = str(no) +'.jpg'
    rq.urlretrieve(url, file_name)

download_web_image('https://thenewboston.com/photos/users/2/resized/869b40793dc9aa91a438b1eb6ceeaa96.jpg')