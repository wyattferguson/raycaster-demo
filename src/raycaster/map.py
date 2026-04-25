import math

from .config import MAP, TILE_SIZE


def xy_to_map_tiles(x: float, y: float) -> tuple[int, int]:
    """Convert x/y into map coordinates."""
    col = int(x / TILE_SIZE)
    row = int(y / TILE_SIZE)
    return col, row


def xy_cast(
    x: float,
    y: float,
    angle: float,
    depth: float,
) -> tuple[float, float, int, int]:
    """Calculate x/y position into the world."""
    new_x = x + math.sin(angle) * depth
    new_y = y + math.cos(angle) * depth
    tile_col, tile_row = xy_to_map_tiles(new_x, new_y)
    return (new_x, new_y, tile_col, tile_row)


def tile_at(col: int, row: int) -> int:
    """Read map tile value with boundary-safe wall fallback."""
    if row < 0 or row >= len(MAP):
        return 1
    if col < 0 or col >= len(MAP[row]):
        return 1
    return MAP[row][col]
