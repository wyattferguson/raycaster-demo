import math

import pygame as pg

from config import *


class Player():
    def __init__(self, screen) -> None:
        self.speed = 10
        self.x = SCREEN_WIDTH // 2
        self.y = SCREEN_HEIGHT // 2
        self.angle = math.pi  # face straight up
        self.rot_speed = 0.075
        self.size = 10
        self.fov = math.pi / 3
        self.hfov = self.fov / 2
        self.screen = screen

    def move(self):
        speed_sin = self.speed * math.sin(self.angle)
        speed_cos = self.speed * math.cos(self.angle)

        keys = pg.key.get_pressed()
        if keys:
            dx, dy = 0, 0
            # move player x/y
            if keys[pg.K_w]:
                dx += speed_cos
                dy += speed_sin
            if keys[pg.K_s]:
                dx += -speed_cos
                dy += -speed_sin
            if keys[pg.K_a]:
                dx += speed_sin
                dy += -speed_cos
            if keys[pg.K_d]:
                dx += -speed_sin
                dy += speed_cos

            self.x += dx
            self.y += dy

            # rotate player
            if keys[pg.K_j]:
                self.angle -= self.rot_speed
            if keys[pg.K_l]:
                self.angle += self.rot_speed

            self.angle %= math.tau

    def draw(self):
        pg.draw.circle(self.screen, RED, (self.x, self.y), self.size)

        pg.draw.line(self.screen, YELLOW,
                     (self.x, self.y),
                     (self.x + math.cos(self.angle) * 50, self.y + math.sin(self.angle) * 50), 2)
