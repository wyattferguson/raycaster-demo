import pygame as pg

from .config import MAP, PLAYER_SIZE, RED, SCALER, TILE_SIZE, WHITE, YELLOW, Color
from .map import xy_cast
from .player import Player


class MiniMap:
    """Mini map showing player position and walls."""

    def __init__(self, player: Player) -> None:
        self.surface = pg.display.get_surface()
        self.map = MAP
        self.tile_spacer = SCALER / 2
        self.player = player

    def draw(self) -> None:
        """Draw mini map."""
        for y, row in enumerate(self.map):
            for x, tile in enumerate(row):
                if tile:
                    self.draw_tile(x, y, WHITE)

        self.draw_player(self.player.x, self.player.y, self.player.angle)

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

    def draw_player(self, x: float, y: float, angle: float) -> None:
        """Draw player position on mini map."""
        # draw player circle on mini map
        pg.draw.circle(self.surface, RED, (x, y), PLAYER_SIZE)

        # draw player direction line on mini map
        dx, dy, *_ = xy_cast(x, y, angle, SCALER)
        pg.draw.line(self.surface, YELLOW, (x, y), (dx, dy), 2)
