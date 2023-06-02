import pygame as pg

from config import RED


class Player():
    def __init__(self, screen) -> None:
        self.speed = 10
        self.x = 125
        self.y = 250
        self.width = 15
        self.height = 15
        self.screen = screen

    def move(self,direction:tuple):
        self.x += direction[0] * self.speed
        self.y += direction[1] * self.speed

    def draw(self):
        pg.draw.rect(
            self.screen,
            RED,
            pg.Rect(
                self.x,
                self.y,
                self.width,
                self.height
            ),
        )