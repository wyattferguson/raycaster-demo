import pygame as pg

from config import *


class Board():
    def __init__(self, screen) -> None:
        self.screen = screen
        self.map = [
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 1, 0, 0, 0, 0, 1],
            [1, 0, 1, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 1, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1]
        ]
        self.tile_width = SCREEN_WIDTH // len(self.map[0])
        self.tile_height = SCREEN_HEIGHT // len(self.map)
        self.spacer = 2

    def draw(self):
        for y, row in enumerate(self.map):
            for x, tile in enumerate(row):
                if tile:
                    self.rect(x, y, WHITE)

    def blank(self):
        self.screen.fill(BLACK)

    def rect(self, x: int, y: int, color):
        pg.draw.rect(
            self.screen,
            color,
            pg.Rect(
                x * self.tile_width + self.spacer,
                y * self.tile_height + self.spacer,
                self.tile_width - self.spacer,
                self.tile_height - self.spacer
            ),
        )
