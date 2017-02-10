#   28. CSV

import csv

with open('s28.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    dates=[]
    colors=[]
    for row in readCSV :
        date = row[0]
        color = row[3]
        dates.append(date)
        colors.append(color)
    print(dates)
    print(colors)
    qColor = input('Choose color for dates? ')
    index = colors.index(qColor.lower())
    print('Date for',qColor,'is :', dates[index])



