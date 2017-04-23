#   calculates youtube playlist duration
#   need to work directly on web
import csv

with open('time.txt') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=':')
    days = 0
    hrs = 0
    mins = 0
    secs = 0
    for t in readCSV:
        # skip blank line and comments
        if not t:
            pass
        elif t[0][0] == '#':
            pass
        # count time
        else:
            if len(t)>2:
                hrs += int(t[0])
                mins += int(t[1])
                secs += int(t[2])
            else:
                mins += int(t[0])
                secs += int(t[1])
            if hrs >= 24:
                days += 1
                hrs -= 24
            if mins >= 60:
                hrs += 1
                mins -= 60
            if secs >= 60:
                mins += 1
                secs -= 60
        #print(t, days, hrs, mins, secs)
    print('Playlist duration',str(days)+'d',str(hrs)+'h',str(mins)+'m',str(secs)+'s')
