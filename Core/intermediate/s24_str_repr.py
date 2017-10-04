import pygame
from Core.intermediate.blob24 import Blob
import numpy as np
import logging
import datetime

'''
DEBUG INFO WARNING ERROR CRITICAL
'''

# logging.basicConfig(level=logging.INFO, filename="s22_logging.txt")
logging.basicConfig(level=logging.INFO)
STARTING_RED_BLOBS = 15
STARTING_GREEN_BLOBS = 15
STARTING_BLUE_BLOBS = 15

WIDTH = 600
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
        logging.info("{} Blue collides with {}".format(datetime.datetime.now(), repr(other_blob)))
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


def is_touching(b1, b2):
    # dist = ((b1.x - b2.x)**2 + (b1.y - b2.y)**2)**0.5
    dist = np.linalg.norm(np.array([b1.x, b1.y])-np.array([b2.x, b2.y]))
    return dist < (b1.size + b2.size)


def handle_collisions(blobs_list):
    red_blobs, green_blobs, blue_blobs = blobs_list
    for blue_id, blue_blob in blue_blobs.copy().items():
        for other_blobs in red_blobs, green_blobs, blue_blobs:
            for other_id, other_blob in other_blobs.copy().items():
                logging.debug("{} Checking {} & {} collision".format(datetime.datetime.now(), repr(blue_blob), repr(other_blob)))
                if other_blob == blue_blob:
                    pass
                else:
                    if is_touching(blue_blob, other_blob):
                        blue_blob + other_blob
                        if other_blob.size <= 0:
                            logging.warning("{} {} deleted".format(datetime.datetime.now(), str(other_blob)))
                            del other_blobs[other_id]
                        if blue_blob.size <= 0:
                            logging.warning("{} {} deleted".format(datetime.datetime.now(), str(blue_blob)))
                            del blue_blobs[blue_id]
    return red_blobs, green_blobs, blue_blobs


# def clean_up(blobs_list):
#     for blobs in blobs_list:
#         for blob_id in blobs.copy():
#             if blobs[blob_id].size < 0:
#                 print("Deleted!")
#                 del blobs[blob_id]
#     return blobs_list


def draw_environment(blobs_list):
    red_blobs, green_blobs, blue_blobs = handle_collisions(blobs_list)
    # red_blobs, green_blobs, blue_blobs = clean_up([red_blobs, green_blobs, blue_blobs])
    game_display.fill(WHITE)
    for blobs_dict in blobs_list:
        for blob_id in blobs_dict:
            blob = blobs_dict[blob_id]
            pygame.draw.circle(game_display, blob.color, (blob.x, blob.y), blob.size)
            blob.move()
            blob.check_bounds()
    pygame.display.update()
    return red_blobs, green_blobs, blue_blobs


def main():
    red_blobs = dict(enumerate([RedBlob(WIDTH, HEIGHT) for _ in range(STARTING_RED_BLOBS)]))
    green_blobs = dict(enumerate([GreenBlob(WIDTH, HEIGHT) for _ in range(STARTING_GREEN_BLOBS)]))
    blue_blobs = dict(enumerate([BlueBlob(WIDTH, HEIGHT) for _ in range(STARTING_BLUE_BLOBS)]))
    try:
        # A+B
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            red_blobs, green_blobs, blue_blobs = draw_environment([red_blobs, green_blobs, blue_blobs])
            clock.tick(60)
    except Exception as e:
        logging.critical(str(e))


if __name__ == "__main__":
    # print(datetime.datetime.now())
    # print(repr(datetime.datetime.now()))
    # print(str(datetime.datetime.now()))

    # red_blobs = dict(enumerate([RedBlob(WIDTH, HEIGHT) for _ in range(STARTING_RED_BLOBS)]))
    # green_blobs = dict(enumerate([GreenBlob(WIDTH, HEIGHT) for _ in range(STARTING_GREEN_BLOBS)]))
    # blue_blobs = dict(enumerate([BlueBlob(WIDTH, HEIGHT) for _ in range(STARTING_BLUE_BLOBS)]))
    # print(blue_blobs[0])
    # print(repr(blue_blobs[0]))
    # print(str(blue_blobs[0]))
    # pygame.quit()

    main()
