import random

WIDTH = 0
HEIGHT = 0


class Blob:

    def __init__(self, color):
        self.color = color
        self.x = random.randrange(0, WIDTH)
        self.y = random.randrange(0, HEIGHT)
        self.size = random.randrange(4, 8)

    def move(self):
        self.x += random.randrange(-1, 2)
        self.y += random.randrange(-1, 2)
        if self.x < 0:
            self.x = 0
        elif self.x > WIDTH:
            self.y = WIDTH
        if self.y < 0:
            self.y = 0
        elif self.y > HEIGHT:
            self.y = HEIGHT
