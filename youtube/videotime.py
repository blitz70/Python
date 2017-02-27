#   calculates youtube playlist duration
#   need to work directly on web
import csv

with open('geof.txt') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=':')
    day = 0
    hr = 0
    min = 0
    sec = 0
    for t in readCSV:
        if not t:
           pass
        else:
            #print(t)
            if len(t)>2:
                hr += int(t[0])
                min += int(t[1])
                sec += int(t[2])
            else:
                min += int(t[0])
                sec += int(t[1])
            if hr >= 24:
                day += 1
                hr -= 24
            if min >= 60:
                hr += 1
                min -= 60
            if sec >= 60:
                min += 1
                sec -= 60
        #print(t, day, hr, min, sec)
    print('Playlist duration',str(day)+'d',str(hr)+'h',str(min)+'m',str(sec)+'s')
