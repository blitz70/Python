#class : multiple inheritance

class Sense:
    def eye(self):
        print('I can see')
    def ear(self):
        print('I can hear')
    def nose(self):
        print('I can smell')

class Action:
    def leg(self):
        print('I can run')
    def arm(self):
        print('I can lift')

class Human:
    def brain(self):
        print('I can understand')

class Person(Sense, Action, Human):
    pass

p1 = Person()

p1.eye()
p1.arm()
p1.brain()
