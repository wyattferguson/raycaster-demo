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

            move_x = self.x + math.sin(self.angle) * direction
            move_y = self.y + math.cos(self.angle) * direction
            if not self.collision(move_x, move_y):
                self.x = move_x
                self.y = move_y

            # rotate player
            if keys[pg.K_a]:
                self.angle += self.rot_speed
            elif keys[pg.K_d]:
                self.angle -= self.rot_speed

            self.angle %= math.tau  # wrap around angle

    def collision(self, x: int, y: int) -> bool:
        # does the next move hit a wall tile
        next_x = x + math.sin(self.angle) * self.hit_depth
        next_y = y + math.cos(self.angle) * self.hit_depth
        col, row = self.xy_to_tile_coords(next_x, next_y)
        return MAP[row][col] == 1

    def draw(self):
        # draw player circle
        pg.draw.circle(self.screen, RED, (self.x, self.y), self.size)

        # draw direction line
        pg.draw.line(self.screen, YELLOW, (self.x, self.y), (self.x + math.sin(self.angle)
                     * self.hit_depth, self.y + math.cos(self.angle) * self.hit_depth), 2)

        #  # draw player FOV cone
        # pg.draw.line(self.screen, GREEN, (self.x, self.y),
        #                                 (self.x + math.sin(self.angle - self.hfov) * 50,
        #                                     self.y + math.cos(self.angle - self.hfov) * 50), 2)

        # pg.draw.line(self.screen, GREEN, (self.x, self.y),
        #                                 (self.x + math.sin(self.angle + self.hfov) * 50,
        #                                     self.y + math.cos(self.angle + self.hfov) * 50), 2)
        self.raycaster()

    def xy_to_tile_coords(self, x: int, y: int) -> tuple:
        col = int(x / TILE_WIDTH)
        row = int(y / TILE_HEIGHT)
        return col, row

    def raycaster(self):
        # start at left side of cone
        start_angle = self.angle - self.hfov

        for ray in range(self.rays):
            for depth in range(self.view_depth):

                # get ray target coordinates
                target_x = self.x + math.sin(start_angle) * depth
                target_y = self.y + math.cos(start_angle) * depth

                # covert target X, Y coordinate to map col, row
                col, row = self.xy_to_tile_coords(target_x, target_y)

                # ray hits a map wall
                if MAP[row][col] == 1:
                    # draw casted ray
                    pg.draw.line(self.screen, GREEN, (self.x, self.y), (target_x, target_y))
                    break

            start_angle += self.step_angle
