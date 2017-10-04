import matplotlib.pyplot as plt

def blog_post1(arg, *args):
    print(arg)
    [print(i) for i in args]


def blog_post2(arg, **kwargs):
    print(arg)
    [print(i, v) for i, v in kwargs.items()]


def blog_post3(arg, *args, **kwargs):
    print(arg)
    [print(i) for i in args]
    [print(i, v) for i, v in kwargs.items()]


blog_0 = "This is my blog!"
blog_1 = "My name is Sung."
blog_2 = "I am leaning to code."
blog_3 = "I like Python."
blog_post1(blog_0, blog_1, blog_2, blog_3)
blog_post2(blog_0, b1=blog_1, b2=blog_2, b3=blog_3)
blog_post3(blog_0,
           "one", "two", "three",
           b1=blog_1, b2=blog_2, b3=blog_3,)


def graph_function(x, y):
    print("function that graphs {} and {}".format(x, y))
    plt.plot(x, y, label="{} {}".format(x, y))
    plt.title("SOME GRAPH")
    plt.xlabel("x-axis")
    plt.ylabel("y-axis")
    plt.legend()
    plt.grid()
    plt.show()


x1 = [1, 2, 3]
y1 = [30, 10, 20]
graph = [y1, x1]
graph_function(x1, y1)
graph_function(*graph)

