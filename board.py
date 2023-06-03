import pygame as pg

from config import *


class Board():
    def __init__(self, screen) -> None:
        self.screen = screen
        self.map = MAP
        self.tile_spacer = 2


    def draw(self):
        for y, row in enumerate(self.map):
            for x, tile in enumerate(row):
                if tile:
                    self.tile(x, y, WHITE)

    def blank(self):
        self.screen.fill(BLACK)

    def tile(self, x: int, y: int, color):
        pg.draw.rect(
            self.screen,
            color,
            pg.Rect(
                x * TILE_SIZE + self.tile_spacer,
                y * TILE_SIZE + self.tile_spacer,
                TILE_SIZE - self.tile_spacer,
                TILE_SIZE - self.tile_spacer
            ),
        )
