# data structure : searching and sorting
# complex list of dictionaries with multiple keys

import operator

people = [
    {'firstname': 'Arnold', 'lastname': 'Schwarzenegger'},
    {'firstname': 'SK', 'lastname': 'Kim'},
    {'firstname': 'Tom', 'lastname': 'Jones'},
    {'firstname': 'John', 'lastname': 'Woo'},
    {'firstname': 'Sylvester', 'lastname': 'Stallone'},
    {'firstname': 'CM', 'lastname': 'Kim'},
    {'firstname': 'Whoopi', 'lastname': 'Goldberg'},
    {'firstname': 'Leonard', 'lastname': 'Nimoy'},
    {'firstname': 'John', 'lastname': 'Doe'},
    {'firstname': 'Dolph', 'lastname': 'Lundgren'},
    {'firstname': 'TK', 'lastname': 'Kim'},
    {'firstname': 'John', 'lastname': 'McEnroe'},
    {'firstname': 'Anne', 'lastname': 'Hathaway'},
    {'firstname': 'Patric', 'lastname': 'Steward'},
]

# operator.itemgetter method
print('itemgetter : wrong')
for item in sorted(people, key=operator.itemgetter('firstname')):
    print(item)
print('itemgetter : correct')
for item in sorted(people, key=operator.itemgetter('firstname', 'lastname')):
    print(item)

# lambda method
print('lambda : wrong')
for item in sorted(people, key=lambda x: x['lastname']):
    print(item)
print('lambda : correct')
for item in sorted(people, key=lambda x: (x['lastname'], x['firstname'])):
    print(item)