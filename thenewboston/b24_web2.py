#web : download file

import urllib.request as rq

goog_url = 'http://chart.finance.yahoo.com/table.csv?s=GOOG&a=2&b=4&c=2017&d=3&e=4&f=2017&g=d&ignore=.csv'

def download_stock_data(csv_url):
    resp = rq.urlopen(csv_url)
    csv = resp.read()
    lines = str(csv).split(r'\n')
    print(len(lines))
    print(lines)
    fw = open(r'goog.csv','w')
    for line in lines:
        fw.write(line+'\n')
    fw.close()

download_stock_data(goog_url)