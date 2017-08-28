import random
import pygame

WIDTH = 800
HEIGHT = 600
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

game_display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Blob World")
clock = pygame.time.Clock()


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


def draw_environment(blob):
    game_display.fill(WHITE)
    pygame.draw.circle(game_display, blob.color, (blob.x, blob.y), blob.size)
    pygame.display.update()
    # print(blob.x, blob.y)
    blob.move()


def main():
    red_blob = Blob(RED)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        draw_environment(red_blob)
        clock.tick(60)

if __name__ == "__main__":
    main()
