import pygame as pg

from config import *


class Board():
    def __init__(self, screen) -> None:
        self.screen = screen
        self.map = MAP
        self.tile_spacer = 2
        # self.tile_width = SCREEN_WIDTH // len(self.map[0])
        # self.tile_height = SCREEN_HEIGHT // len(self.map)

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
                x * TILE_WIDTH + self.tile_spacer,
                y * TILE_HEIGHT + self.tile_spacer,
                TILE_WIDTH - self.tile_spacer,
                TILE_HEIGHT - self.tile_spacer
            ),
        )
