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
        self.fov = math.pi / 3
        self.hfov = self.fov / 2
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

            self.x += math.sin(self.angle) * direction
            self.y += math.cos(self.angle) * direction

            # rotate player
            if keys[pg.K_a]:
                self.angle += self.rot_speed
            elif keys[pg.K_d]:
                self.angle -= self.rot_speed

            self.angle %= math.tau # wrap around angle

    def draw(self):
        # draw player circle
        pg.draw.circle(self.screen, RED, (self.x, self.y), self.size)

        # draw direction line
        pg.draw.line(self.screen, YELLOW,
                     (self.x, self.y),
                     (self.x + math.sin(self.angle) * 50, self.y + math.cos(self.angle) * 50), 2)
