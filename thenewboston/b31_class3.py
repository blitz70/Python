#class : class vs instance variable

class Person:
    gender = 'female'
    def __init__(self, name):
        self.name = name

g1 = Person('Elsa')
g2 = Person('Anna')

print(g1.name, g1.gender)
print(g2.name, g2.gender)
              
g1.name = 'James'
g1.gender = 'male'

print(g1.name, g1.gender)
print(g2.name, g2.gender)
