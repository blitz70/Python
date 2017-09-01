import pygame
from Core.intermediate.blob import Blob

STARTING_RED_BLOBS = 13
STARTING_GREEN_BLOBS = 50
STARTING_BLUE_BLOBS = 100

WIDTH = 800
HEIGHT = 600
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

game_display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Blob World")
clock = pygame.time.Clock()


def draw_environment(blobs_dict):
    game_display.fill(WHITE)
    for blob_id in blobs_dict:
        blob = blobs_dict[blob_id]
        pygame.draw.circle(game_display, blob.color, (blob.x, blob.y), blob.size)
        blob.move()
        # blob.check_bounds()
    pygame.display.update()


def main():
    red_blobs = [Blob(RED, WIDTH, HEIGHT, size_range=(20, 41), movement_range=(-2, 3)) for _ in range(STARTING_RED_BLOBS)]
    green_blobs = [Blob(GREEN, WIDTH, HEIGHT) for _ in range(STARTING_GREEN_BLOBS)]
    blue_blobs = [Blob(BLUE, WIDTH, HEIGHT, size_range=(2, 5), movement_range=(-8, 9)) for _ in range(STARTING_BLUE_BLOBS)]
    blobs = dict(enumerate(blue_blobs + green_blobs + red_blobs))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        draw_environment(blobs)
        clock.tick(60)

if __name__ == "__main__":
    main()
