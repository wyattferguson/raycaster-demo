import math

import pygame as pg

from config import *


class Player():
    def __init__(self, screen) -> None:
        self.speed = 5
        self.x = SCREEN_WIDTH // 2
        self.y = SCREEN_HEIGHT // 2
        self.angle = math.pi  # face straight up
        self.rot_speed = 0.075
        self.size = 10
        self.hit_depth = self.size + 4
        self.view_depth = SCREEN_HEIGHT
        self.fov = math.pi / 3
        self.hfov = self.fov / 2
        self.rays = 120
        self.step_angle = self.fov / self.rays
        self.screen = screen

    def update(self):
        keys = pg.key.get_pressed()
        if keys:
            direction = 0
            # move player forward/back
            if keys[pg.K_w]:
                direction = self.speed
            elif keys[pg.K_s]:
                direction = -self.speed

            # Does next move hit a wall
            dx, dy, col, row = self.xy_cast(self.x, self.y, self.angle, direction)
            if MAP[row][col] == 0:
                self.x = dx
                self.y = dy

            # rotate player
            if keys[pg.K_a]:
                self.angle += self.rot_speed
            elif keys[pg.K_d]:
                self.angle -= self.rot_speed

            self.angle %= math.tau  # wrap around angle

    def draw(self):
        # draw player circle
        pg.draw.circle(self.screen, RED, (self.x, self.y), self.size)

        # draw direction line
        dx, dy, *_ = self.xy_cast(self.x, self.y, self.angle, self.hit_depth)
        pg.draw.line(self.screen, YELLOW, (self.x, self.y), (dx, dy), 2)

        self.raycaster()

    def xy_to_map_tiles(self, x: int, y: int) -> tuple:
        '''convert x/y into map coordiantes'''
        col = int(x / TILE_WIDTH)
        row = int(y / TILE_HEIGHT)
        return col, row

    def xy_cast(self, x: int, y: int, angle: float, depth: float) -> tuple:
        '''calculate x/y position into the world'''
        new_x = x + math.sin(angle) * depth
        new_y = y + math.cos(angle) * depth
        tile_col, tile_row = self.xy_to_map_tiles(new_x, new_y)
        return (new_x, new_y, tile_col, tile_row)

    def raycaster(self):
        # start at left side of the FOV cone
        cast_angle = self.angle - self.hfov

        for ray in range(self.rays):
            for depth in range(self.view_depth):

                dx, dy, col, row = self.xy_cast(self.x, self.y, cast_angle, depth)

                # ray hits a map wall
                if MAP[row][col] == 1:
                    # draw casted ray
                    pg.draw.line(self.screen, GREEN, (self.x, self.y), (dx, dy))
                    break

            # move across the POV arc
            cast_angle += self.step_angle
