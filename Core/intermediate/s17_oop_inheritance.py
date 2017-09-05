import pygame
import random
from Core.intermediate.blob17 import Blob

STARTING_RED_BLOBS = 3
STARTING_BLUE_BLOBS = 10

WIDTH = 800
HEIGHT = 600
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

game_display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Blob World")
clock = pygame.time.Clock()


class BlueBlob(Blob):
    def __init__(self):
        super().__init__(BLUE, WIDTH, HEIGHT)

    def move_fast(self):
        self.x += random.randrange(*self.movement)*7
        self.y += random.randrange(*self.movement)*7


def draw_environment(blobs_dict):
    game_display.fill(WHITE)
    for blob_id in blobs_dict:
        blob = blobs_dict[blob_id]
        pygame.draw.circle(game_display, blob.color, (blob.x, blob.y), blob.size)
        blob.move_fast()
        # blob.check_bounds()
    pygame.display.update()


def main():
    red_blobs = [BlueBlob() for _ in range(STARTING_RED_BLOBS)]
    blue_blobs = [BlueBlob() for _ in range(STARTING_BLUE_BLOBS)]
    blobs = dict(enumerate(blue_blobs + red_blobs))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        draw_environment(blobs)
        clock.tick(60)

if __name__ == "__main__":
    main()
