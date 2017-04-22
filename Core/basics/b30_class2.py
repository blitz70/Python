#class : constructor __init__

class Tuna:
    def __init__(self):
        print("I'm a Tuna")
    def food(self):
        print("I'm your breakfast for today")

tuna = Tuna()
tuna.food()

class Enemy:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
    def info(self):
        print(self.name + ' has', self.hp, 'hp')

enemy1 = Enemy('Minion', 5)
enemy2 = Enemy('Boss', 100)
enemy1.info()
enemy2.info()
              
