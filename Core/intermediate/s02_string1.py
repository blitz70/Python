import os

names = ["Jeff", "Gary", "Jill", "Samantha"]
for name in names:
    print("Hello, " + name)
for name in names:
    print(" ".join(["Hello,", name]))
str = ""
for name in names:
    if str == "":
        str +=  name
    else:
        str = str + ", " + name
print(str)
print(", ".join(names))

file_location = "D:\\CODE\\Git\\Python\\Core\\Intermediate"
file_name = "s01.txt"
with open(file_location + "\\" + file_name) as f1:
    print(f1.read())
with open(os.path.join(file_location, file_name)) as f2:
    print(f2.read())

# Gary bought 12 apples today!
who = "Gary"
how_many = 12
print(who, "bought", how_many, "apples today!")
print("{} bought {} apples today!".format(who, how_many))
print("{f1} bought {f2} apples today!".format(f2=how_many, f1=who))
