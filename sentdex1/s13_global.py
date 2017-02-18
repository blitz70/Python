#   13. Global & Local Variables

x = 6
y = 11

def example():
    z = 5
    print('z=',z)
    global x
    x += 1
    print('x=',x)

example()
print('x=',x)

def example2():
    globX = x
    print('globX=',globX)
    globX +=10
    print('globX=',globX)
    return globX
    
x = example2()
print('x=',x)

