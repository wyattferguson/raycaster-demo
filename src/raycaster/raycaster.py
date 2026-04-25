import math

import pygame as pg

from .config import (
    GREEN,
    MAP,
    MAP_SIZE,
    PLAYER_FOV,
    PLAYER_HFOV,
    RAYS,
    RED,
    SCALER,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    TILE_SIZE,
    WALL_SCALER,
    YELLOW,
)
from .map import tile_at, xy_cast, xy_to_map_tiles
from .player import Player


class Raycaster:
    """Raycasting logic and rendering."""

    def __init__(self, player: Player) -> None:
        self.surface = pg.display.get_surface()
        self.player = player
        self.view_depth = MAP_SIZE
        self.fov = PLAYER_FOV
        self.hfov = PLAYER_HFOV
        self.rays = RAYS
        self.wall_scale = (SCREEN_WIDTH - MAP_SIZE) / self.rays
        self.step_angle = self.fov / self.rays

    def _cast_to_wall(self, cast_angle: float) -> tuple[float, float, float]:
        """Cast one ray and return first wall hit depth and position."""
        for depth in range(1, self.view_depth + 1):
            dx, dy, col, row = xy_cast(self.player.x, self.player.y, cast_angle, depth)
            if tile_at(col, row) == 1:
                return float(depth), dx, dy

        dx, dy, _, _ = xy_cast(self.player.x, self.player.y, cast_angle, self.view_depth)
        return float(self.view_depth), dx, dy

    def draw(self) -> None:
        """Cast rays across the FOV and render corresponding wall slices."""
        # start at left side of the FOV cone
        cast_angle = self.player.angle - self.hfov

        for ray in range(self.rays):
            depth, dx, dy = self._cast_to_wall(cast_angle)

            # Draw the ray on the minimap for visibility.
            pg.draw.line(self.surface, GREEN, (self.player.x, self.player.y), (dx, dy))

            # Correct fish-eye distortion by projecting depth to view plane.
            corrected_depth = max(depth * math.cos(self.player.angle - cast_angle), 0.0001)
            wall_height = min((SCREEN_HEIGHT / corrected_depth) * WALL_SCALER, SCREEN_HEIGHT)

            # Fade walls by distance to improve depth perception.
            shading = int(255 / (1 + corrected_depth * corrected_depth * 0.0001))
            wall_section = pg.Rect(
                SCREEN_WIDTH - ray * self.wall_scale,
                (SCREEN_HEIGHT / 2) - wall_height / 2,
                self.wall_scale + 1,
                wall_height,
            )
            pg.draw.rect(self.surface, (shading, shading, shading), wall_section)

            # move across the POV arc
            cast_angle += self.step_angle
