"""Project-wide constants and static scene configuration."""

type Color = tuple[int, int, int]
type MapGrid = tuple[tuple[int, ...], ...]

FPS = 30

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
HALF_HEIGHT = SCREEN_HEIGHT / 2

MAP: MapGrid = (
    (1, 1, 1, 1, 1, 1, 1, 1),
    (1, 0, 1, 0, 0, 0, 1, 1),
    (1, 0, 1, 0, 0, 0, 0, 1),
    (1, 0, 0, 0, 0, 0, 0, 1),
    (1, 0, 0, 0, 1, 1, 0, 1),
    (1, 0, 1, 0, 0, 0, 0, 1),
    (1, 0, 0, 0, 0, 0, 0, 1),
    (1, 1, 1, 1, 1, 1, 1, 1),
)

SCALER = 2
TILE_SIZE = 10 * SCALER
MAP_SIZE = len(MAP) * TILE_SIZE
WALL_SCALER = 20
SCENE_WIDTH = SCREEN_WIDTH - MAP_SIZE
SCENE_X = MAP_SIZE + 5

WHITE: Color = (255, 255, 255)
BLACK: Color = (0, 0, 0)
BLUE: Color = (0, 0, 255)
RED: Color = (255, 0, 0)
YELLOW: Color = (255, 255, 0)
GREEN: Color = (0, 255, 0)
