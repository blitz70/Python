import timeit


def generator_example():
    yield "this"
    yield "is"
    yield "a"
    yield "generator"
    yield "example"
[print(i) for i in generator_example()]

print(timeit.timeit('''
def code_breaker1(combo):
    count = 0
    for c1 in range(10):
        for c2 in range(10):
            for c3 in range(10):
                for c4 in range(10):
                    count += 1
                    # print(c1, c2, c3)
                    if (c1, c2, c3) == combo:
                        # print("Combo found on {} tries!".format(count))
                        return

CORRECT_COMBO = (5, 2, 8, 6)
code_breaker1(CORRECT_COMBO)
''', number=1000))


print(timeit.timeit('''
def code_breaker2(combo):
    def gen():
        for c1 in range(10):
            for c2 in range(10):
                for c3 in range(10):
                    for c4 in range(10):
                        yield (c1, c2, c3)
    count = 0
    for i in gen():
        count += 1
        # print(i)
        if i == combo:
            # print("Combo found on {} tries!".format(count))
            break

CORRECT_COMBO = (5, 2, 8, 6)
code_breaker2(CORRECT_COMBO)
''', number=1000))
