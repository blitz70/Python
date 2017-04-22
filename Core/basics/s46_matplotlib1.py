#   46. matplotlib - intro
#   47. matplotlib - labels and titles
#   48. matplotlib - styles
#   49. matplotlib - legends
#   50. matplotlib - scatter plots and bar charts
#   51. matplotlib - csv

#   install module
#   pip install -U pip setuptools
#   pip install matplotlib

from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np

#print(style.available)

x1 = [5,6,7,8]
y1 = [7,3,8,3]
x2 = [5,6,7,8]
y2 = [6,7,2,6]

x3 = [3,5,7,9]
y3 = [7,3,8,3]
x4 = [2,4,6,8]
y4 = [6,7,2,6]

#plt.plot([5,6,7,8],[7,3,8,3])
plt.figure(1)
plt.subplot(211)
plt.plot(x1,y1,'g',linewidth=5,label='line one')
plt.plot(x2,y2,'cyan',linewidth=10,label='line two')
plt.title('My chart')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.grid(True,color='black')

plt.figure(1)
style.use('grayscale')
plt.subplot(212)
plt.scatter(x1,y1,color='r')
plt.scatter(x2,y2,color='b')

plt.figure(2)
style.use('dark_background')
plt.subplot(121)
plt.bar(x3,y3,color='r',align='center')
plt.bar(x4,y4,color='b',align='center')

plt.figure(2)
style.use('ggplot')
plt.subplot(122)
x,y = np.loadtxt('s46.csv'
                 ,unpack=True
                 ,delimiter=',')
plt.plot(x,y,label='s46.csv')
plt.legend()

plt.show()

