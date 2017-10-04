import random


class Blob:

    def __init__(self, color, x_boundary, y_boundary, size_range=(4, 8), movement_range=(-1, 2)):
        self.color = color
        self.x_boundary = x_boundary
        self.y_boundary = y_boundary
        self.x = random.randrange(0, self.x_boundary)
        self.y = random.randrange(0, self.y_boundary)
        self.size = random.randrange(*size_range)
        self.movement = movement_range

    def __repr__(self):
        return "[{s.color}, {s.size}, ({s.x}, {s.y})]".format(s=self)

    def __str__(self):
        return "Blob of color {self.color} and size {self.size}, at location ({self.x}, {self.y})]".format(self=self)

    def move(self):
        self.x += random.randrange(*self.movement)
        self.y += random.randrange(*self.movement)

    def check_bounds(self):
        if self.x < 0:
            self.x = 0
        elif self.x > self.x_boundary:
            self.x = self.x_boundary
        if self.y < 0:
            self.y = 0
        elif self.y > self.y_boundary:
            self.y = self.y_boundary
