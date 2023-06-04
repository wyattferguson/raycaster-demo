import pygame as pg

from config import *


class Board():
    def __init__(self, screen) -> None:
        self.screen = screen
        self.map = MAP
        self.tile_spacer = SCALER / 2


    def draw(self):
        '''Draw mini map'''
        for y, row in enumerate(self.map):
            for x, tile in enumerate(row):
                if tile:
                    self.tile(x, y, WHITE)

    def blank(self):
        '''refresh screen'''
        self.screen.fill(BLACK)

        # draw sky
        pg.draw.rect(self.screen, BLACK, pg.Rect(
                MAP_SIZE + 5,
                0,
                SCREEN_WIDTH - MAP_SIZE,
                SCREEN_HEIGHT / 2,
            ))

        # draw floor
        pg.draw.rect(self.screen, BROWN, pg.Rect(
                MAP_SIZE + 5,
                SCREEN_HEIGHT / 2,
                SCREEN_WIDTH - MAP_SIZE,
                SCREEN_HEIGHT / 2,
            ))


    def tile(self, x: int, y: int, color):
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
