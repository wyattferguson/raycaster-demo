import pygame as pg

from config import MAP, SCALER, TILE_SIZE


class MiniMap():
    def __init__(self, screen) -> None:
        self.screen = screen
        self.map = MAP
        self.tile_spacer = SCALER / 2

    def draw(self):
        '''Draw mini map'''
        for y, row in enumerate(self.map):
            for x, tile in enumerate(row):
                if tile:
                    self.tile(x, y, pg.Color("white"))

    def tile(self, x: int, y: int, color: pg.Color):
        '''draw single mini map tile'''
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
