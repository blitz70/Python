import pygame
import random
from Core.intermediate.blob17 import Blob

STARTING_RED_BLOBS = 15
STARTING_GREEN_BLOBS = 15
STARTING_BLUE_BLOBS = 15

WIDTH = 800
HEIGHT = 600
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

game_display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Blob World")
clock = pygame.time.Clock()


class RedBlob(Blob):
    def __init__(self, x_boundary, y_boundary):
        super().__init__((255, 0, 0), x_boundary, y_boundary)


class GreenBlob(Blob):
    def __init__(self, x_boundary, y_boundary):
        super().__init__((0, 255, 0), x_boundary, y_boundary)


class BlueBlob(Blob):
    def __init__(self, x_boundary, y_boundary):
        super().__init__((0, 0, 255), x_boundary, y_boundary)

    def __add__(self, other_blob):
        if other_blob.color == (255, 0, 0):
            self.size -= other_blob.size
            other_blob.size -= self.size
        elif other_blob.color == (0, 255, 0):
            self.size += other_blob.size
            other_blob.size = 0
        elif other_blob.color == self.color:  # nothing
            pass
        else:
            raise Exception("Blob is not Red, Green nor Blue")


def draw_environment(blobs_dict):
    game_display.fill(WHITE)
    for blob_id in blobs_dict:
        blob = blobs_dict[blob_id]
        pygame.draw.circle(game_display, blob.color, (blob.x, blob.y), blob.size)
        blob.move()
        blob.check_bounds()
    pygame.display.update()


def main():
    red_blobs = [RedBlob(WIDTH, HEIGHT) for _ in range(STARTING_RED_BLOBS)]
    green_blobs = [GreenBlob(WIDTH, HEIGHT) for _ in range(STARTING_GREEN_BLOBS)]
    blue_blobs = [BlueBlob(WIDTH, HEIGHT) for _ in range(STARTING_BLUE_BLOBS)]
    blobs = dict(enumerate(blue_blobs + green_blobs + red_blobs))
    # while True:
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             pygame.quit()
    #             quit()
    #     draw_environment(blobs)
    #     clock.tick(60)
    print("Blue size:{}, Red size:{}".format(blue_blobs[0].size, red_blobs[0].size))
    blue_blobs[0] + red_blobs[0]
    print("Blue size:{}, Red size:{}".format(blue_blobs[0].size, red_blobs[0].size))

if __name__ == "__main__":
    main()
