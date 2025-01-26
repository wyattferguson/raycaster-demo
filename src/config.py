FPS = 30
SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = (800, 500)
HALF_HEIGHT = SCREEN_HEIGHT / 2

MAP = [
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 0, 0, 1, 1],
    [1, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],
]

SCALER = 2
TILE_SIZE = 10 * SCALER
MAP_SIZE = len(MAP) * TILE_SIZE
WALL_SCALER = 20
SCENE_WIDTH = SCREEN_WIDTH - MAP_SIZE
SCENE_X = MAP_SIZE + 5
