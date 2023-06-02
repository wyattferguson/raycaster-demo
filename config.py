# pygame settings
FPS = 60
SCREEN_SIZE = SCREEN_HEIGHT, SCREEN_WIDTH = (800, 800)

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREY = (84, 84, 84)
GREEN = (0, 255, 0)


# map

MAP = [
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 1, 0, 0, 0, 0, 1],
            [1, 0, 1, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 1, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1]
        ]

TILE_SIZE = SCREEN_HEIGHT // len(MAP)