import random
import pygame

STARTING_RED_BLOBS = 3
STARTING_BLUE_BLOBS = 10

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


def draw_environment(blobs_dict):
    game_display.fill(WHITE)
    for blob_id in blobs_dict:
        blob = blobs_dict[blob_id]
        pygame.draw.circle(game_display, blob.color, (blob.x, blob.y), blob.size)
        blob.move()
    pygame.display.update()


def main():
    red_blobs = [Blob(RED) for _ in range(STARTING_RED_BLOBS)]
    blue_blobs = [Blob(BLUE) for _ in range(STARTING_BLUE_BLOBS)]
    blobs = dict(enumerate(red_blobs + blue_blobs))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        draw_environment(blobs)
        clock.tick(60)

if __name__ == "__main__":
    main()
