# data structure : searching and sorting
# objects by member variables

import operator

class User:
    def __init__(self, u_name, u_id, u_age, u_sex):
        self.u_name = u_name
        self.u_id = u_id
        self.u_age = u_age
        self.u_sex = u_sex
    def __repr__(self):
        return str(self.u_id) + '\t' + self.u_name + '\t' + str(self.u_age) + '\t' + self.u_sex

users = [
    User('Bucky', 43, 32, 'Male'),
    User('Sally', 5, 26, 'Female'),
    User('Tuna', 61, 1, 'Fish'),
    User('Brian', 2, 42, 'Male'),
    User('Judy', 77, 57, 'Female'),
    User('Amanda', 9, 16, 'Female'),
]

print('Default\nID\tName\tAge\tGender')
for user in users:
    print(user)

print('By ID\nID\tName\tAge\tGender')
for user in sorted(users, key=operator.attrgetter('u_id')):
    print(user)

print('By Name\nID\tName\tAge\tGender')
for user in sorted(users, key=lambda x: x.u_name):
    print(user)

print('By Gender and Age\nID\tName\tAge\tGender')
for user in sorted(users, key=lambda x: (x.u_sex, x.u_age)):
    print(user)
