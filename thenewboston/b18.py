# Unpacking arguments

def person_desc(name, age, job, home):
    desc = name + ' is ' + str(age) + ' years old, and lives in ' + home
    print(desc)

person_desc('John', 48, 'programmer', 'USA')

person = ['Jane', 24,'nurse','Brazil']

person_desc(*person)
