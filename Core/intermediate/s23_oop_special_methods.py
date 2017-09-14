# x = range(5)
x = (i for i in range(5))
print(x, "\n", dir(x))
next(x)
print(next(x))
x.__next__()
for i in x:
    print(i)


class RangeEx:
    def __init__(self, end, step=1):
        self.current = -1
        self.end = end
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration()
        else:
            r = self.current
            self.current += self.step
            return r

x = RangeEx(10)
print(dir(RangeEx), "\n", dir(x))
x.__next__()
next(x)
for i in x:
    print(i)


def range_ex(end):
    current = 0
    while current < end:
        r = current
        current += 1
        yield r

print(range_ex, "\n", range_ex(5), "\n", dir(range_ex), "\n", dir(range_ex(5)))
x = (i for i in range_ex(5))
print(dir(x))
for i in x:
    print(i)
