# data structure, unpacking list, elastic list
my_list = ['Blitz', 'Programmer', 48]
name, job, age = my_list
print(my_list[0], my_list[1], my_list[2])
print(name, job, age)

def my_avg(grades):
    first, *middle, last = grades
    print(middle)
    print(sum(middle)/len(middle))
my_avg([5, 23, 55, 27, 90])
my_avg([45, 66, 28, 5, 23, 55, 27, 90, 28])