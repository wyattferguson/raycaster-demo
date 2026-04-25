import math

import pygame as pg

from .config import (
    PLAYER_ROT_SPEED,
    PLAYER_SIZE,
    PLAYER_START_ANGLE,
    PLAYER_START_X,
    PLAYER_START_Y,
    SCALER,
)
from .map import tile_at, xy_cast


class Player:
    """Player object with position, movement, and raycasting logic."""

    def __init__(
        self,
        start_x: int = PLAYER_START_X,
        start_y: int = PLAYER_START_Y,
        start_angle: float = PLAYER_START_ANGLE,
    ) -> None:

        self.speed = SCALER
        self.x = start_x
        self.y = start_y
        self.angle = start_angle
        self.rot_speed = PLAYER_ROT_SPEED

    def update(self) -> None:
        """Update player movement and orientation from keyboard input."""
        keys = pg.key.get_pressed()
        self._move(keys)
        self._rotate(keys)

    def draw(self) -> None:
        """Draw player."""

    def _move(self, keys: pg.key.ScancodeWrapper) -> None:
        """Move forward/backward only when the destination tile is open."""
        direction = 0.0
        if keys[pg.K_w]:
            direction = self.speed
        elif keys[pg.K_s]:
            direction = -self.speed

        if direction == 0:
            return

        dx, dy, col, row = xy_cast(self.x, self.y, self.angle, direction + 0.5)
        if tile_at(col, row) == 0:
            self.x = dx
            self.y = dy

    def _rotate(self, keys: pg.key.ScancodeWrapper) -> None:
        """Rotate left/right and wrap within full circle."""
        if keys[pg.K_a]:
            self.angle += self.rot_speed
        elif keys[pg.K_d]:
            self.angle -= self.rot_speed

        self.angle %= math.tau
