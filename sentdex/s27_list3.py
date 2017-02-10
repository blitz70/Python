#   27. Multi-dimensional Lists

x = [
        [
            [5,7],
            [6,6]
        ],
        [
            [6,6],
            [7,8]
        ],
        [7,2],
        [2,5]
    ]

print(x)
print(x[0])
print(x[1][1][0])
print(x[2])
print(x[3][1])

def func(*a):
    print(list(a))

func(5,2,3,8,9)
