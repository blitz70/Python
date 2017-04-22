#   37. Parsing websites with re & urllib

import re
import urllib.request as rq, urllib.parse as ps


url = 'https://pythonprogramming.net/parse-website-using-regular-expressions-urllib/'
req = rq.Request(url)
resp = rq.urlopen(req)
respData = resp.read()
#print(respData)

paragraphs = re.findall('<p>(.*?)</p>',str(respData))
for paragraph in paragraphs:
    print(paragraph)

s = '<html><head><title>Title</title>'
result = re.match('<.*?>', s)
print(result.group())
