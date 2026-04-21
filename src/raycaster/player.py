import math

import pygame as pg

from raycaster.config import (
    GREEN,
    MAP,
    MAP_SIZE,
    RED,
    SCALER,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    TILE_SIZE,
    WALL_SCALER,
    YELLOW,
)


class Player:
    """Player object with position, movement, and raycasting logic."""

    def __init__(self) -> None:
        self.surface = pg.display.get_surface()
        self.speed = SCALER
        self.x = (TILE_SIZE * 4) + (TILE_SIZE / 2)
        self.y = (TILE_SIZE * 3) + (TILE_SIZE / 2)
        self.angle = math.pi / 2
        self.rot_speed = 0.075
        self.size = 2.5 * SCALER
        self.hit_depth = self.size + self.speed
        self.view_depth = MAP_SIZE
        self.fov = math.pi / 3
        self.hfov = self.fov / 2
        self.rays = 120
        self.wall_scale = (SCREEN_WIDTH - MAP_SIZE) / self.rays
        self.step_angle = self.fov / self.rays

    def update(self) -> None:
        """Update player movement and orientation from keyboard input."""
        keys = pg.key.get_pressed()
        self._move(keys)
        self._rotate(keys)

    def draw(self) -> None:
        """Draw player marker, facing line, and 3D wall projection."""
        # draw player circle on mini map
        pg.draw.circle(self.surface, RED, (self.x, self.y), self.size)

        # draw direction line on mini map
        dx, dy, *_ = self.xy_cast(self.x, self.y, self.angle, self.hit_depth)
        pg.draw.line(self.surface, YELLOW, (self.x, self.y), (dx, dy), 2)

        self.raycaster()

    def _move(self, keys: pg.key.ScancodeWrapper) -> None:
        """Move forward/backward only when the destination tile is open."""
        direction = 0.0
        if keys[pg.K_w]:
            direction = self.speed
        elif keys[pg.K_s]:
            direction = -self.speed

        if direction == 0:
            return

        dx, dy, col, row = self.xy_cast(self.x, self.y, self.angle, direction)
        if self._tile_at(col, row) == 0:
            self.x = dx
            self.y = dy

    def _rotate(self, keys: pg.key.ScancodeWrapper) -> None:
        """Rotate left/right and wrap within full circle."""
        if keys[pg.K_a]:
            self.angle += self.rot_speed
        elif keys[pg.K_d]:
            self.angle -= self.rot_speed

        self.angle %= math.tau

    def _tile_at(self, col: int, row: int) -> int:
        """Read map tile value with boundary-safe wall fallback."""
        if row < 0 or row >= len(MAP):
            return 1
        if col < 0 or col >= len(MAP[row]):
            return 1
        return MAP[row][col]

    def xy_to_map_tiles(self, x: float, y: float) -> tuple[int, int]:
        """Convert x/y into map coordinates."""
        col = int(x / TILE_SIZE)
        row = int(y / TILE_SIZE)
        return col, row

    def xy_cast(
        self,
        x: float,
        y: float,
        angle: float,
        depth: float,
    ) -> tuple[float, float, int, int]:
        """Calculate x/y position into the world."""
        new_x = x + math.sin(angle) * depth
        new_y = y + math.cos(angle) * depth
        tile_col, tile_row = self.xy_to_map_tiles(new_x, new_y)
        return (new_x, new_y, tile_col, tile_row)

    def _cast_to_wall(self, cast_angle: float) -> tuple[float, float, float]:
        """Cast one ray and return first wall hit depth and position."""
        for depth in range(1, self.view_depth + 1):
            dx, dy, col, row = self.xy_cast(self.x, self.y, cast_angle, depth)
            if self._tile_at(col, row) == 1:
                return float(depth), dx, dy

        dx, dy, _, _ = self.xy_cast(self.x, self.y, cast_angle, self.view_depth)
        return float(self.view_depth), dx, dy

    def raycaster(self) -> None:
        """Cast rays across the FOV and render corresponding wall slices."""
        # start at left side of the FOV cone
        cast_angle = self.angle - self.hfov

        for ray in range(self.rays):
            depth, dx, dy = self._cast_to_wall(cast_angle)

            # Draw the ray on the minimap for visibility.
            pg.draw.line(self.surface, GREEN, (self.x, self.y), (dx, dy))

            # Correct fish-eye distortion by projecting depth to view plane.
            corrected_depth = max(depth * math.cos(self.angle - cast_angle), 0.0001)
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
