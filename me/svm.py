import matplotlib.pyplot as plt, math

x = []
y =[]
for n in range(-20, 20):
    x.append(n)
    y.append(-math.log(1/(1+math.exp(-n))))

plt.figure(1)
plt.plot(x, y)

x = []
y =[]
for n in range(-20, 20):
    x.append(n)
    y.append(-math.log(1-1/(1+math.exp(-n))))

plt.figure(2)
plt.plot(x, y)

x = []
y =[]
for n in range(-20, 20):
    x.append(n)
    y.append(1/(1+math.exp(-n)))

plt.figure(3)
plt.plot(x, y)

plt.show()