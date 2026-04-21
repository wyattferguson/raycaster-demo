import pygame as pg

from raycaster.config import MAP, SCALER, TILE_SIZE, WHITE, Color


class MiniMap:
    """Mini map showing player position and walls."""

    def __init__(self) -> None:
        self.surface = pg.display.get_surface()
        if self.surface is None:
            msg = "Display surface was not initialized before MiniMap creation."
            raise RuntimeError(msg)
        self.map = MAP
        self.tile_spacer = SCALER / 2

    def draw(self) -> None:
        """Draw mini map."""
        for y, row in enumerate(self.map):
            for x, tile in enumerate(row):
                if tile:
                    self.draw_tile(x, y, WHITE)

    def draw_tile(self, x: int, y: int, color: Color) -> None:
        """Draw single mini map tile."""
        pg.draw.rect(
            self.surface,
            color,
            pg.Rect(
                x * TILE_SIZE + self.tile_spacer,
                y * TILE_SIZE + self.tile_spacer,
                TILE_SIZE - self.tile_spacer,
                TILE_SIZE - self.tile_spacer,
            ),
        )
