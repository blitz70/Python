#class and objects

class Calculator:

    param1 = []
    param2 = []

    def param(self, x, y):
        self.param1 = x
        self.param2 = y

    def add(self):
        result = self.param1 + self.param2
        print(result)

    def sub(self):
        result = self.param1 - self.param2
        print(result)

    def mult(self):
        result = self.param1 * self.param2
        print(result)

    def div(self):
        result = self.param1 / self.param2
        print(result)

'''calc = Calculator()
calc.param(2, 5)
calc.mult()
calc.sub()
calc.div()'''

class Enemy:

    life = 6

    def small_attack(self):
        self.life -= 1
        print('Uuh?')

    def med_attack(self):
        self.life -= 2
        print('Outch!')

    def big_attack(self):
        self.life -= 3
        print('OMG!')

    def check_life(self):
        if self.life <= 0:
            print("Ack! I'm dead, I'll be revenged!")
        elif self.life <= 2:
            print("Please don't kill me!")
        elif self.life <= 4:
            print("Not bad, your're an worthy opponent!")
        else:
            print("I'm still kicking and breathing!")

enemy1 = Enemy()
enemy2 = Enemy()

enemy1.small_attack()
enemy1.check_life()
enemy2.check_life()

enemy1.small_attack()
enemy1.check_life()
enemy2.check_life()

enemy2.med_attack()
enemy1.check_life()
enemy2.check_life()

enemy2.big_attack()
enemy1.check_life()
enemy2.check_life()
