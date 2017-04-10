#class : inheritance

class Parent:
    def last_name(self):
        return 'Kim'
    def first_name(self):
        return 'SK'

class Child(Parent):
    def first_name(self):
        return 'Curie'

p1 = Parent()
p2 = Child()

print(p1.first_name(), p1.last_name())
print(p2.first_name(), p2.last_name())
