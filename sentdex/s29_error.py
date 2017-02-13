#   29. Error Handling

import csv


with open('s28.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    dates=[]
    colors=[]
    for row in readCSV:
        date = row[0]
        color = row[3]
        dates.append(date)
        colors.append(color)
print(dates)
print(colors)
try:#use try when control is given to outside
    qColor = input('Choose color for date? ')
    if qColor in colors:
        index = colors.index(qColor.lower())
        print('Date for',qColor,'is :', dates[index])
    else:
        print('No such color')
except Exception as e:
    print(e)
print('EOProgram')
