import pygame as pg

from raycaster.config import HALF_HEIGHT, SCENE_WIDTH, SCENE_X
from raycaster.minimap import MiniMap
from raycaster.player import Player


class Scene:
    def __init__(self, screen) -> None:
        self.screen = screen
        self.mini_map = MiniMap(screen)
        self.objects = [Player(self.screen)]

    def blank(self) -> None:
        """Refresh screen."""
        self.screen.fill(pg.Color("black"))

        self.mini_map.draw()

        # draw sky
        pg.draw.rect(
            self.screen,
            pg.Color("blue"),
            pg.Rect(
                SCENE_X,
                0,
                SCENE_WIDTH,
                HALF_HEIGHT,
            ),
        )

        # draw floor
        pg.draw.rect(
            self.screen,
            pg.Color("brown"),
            pg.Rect(
                SCENE_X,
                HALF_HEIGHT,
                SCENE_WIDTH,
                HALF_HEIGHT,
            ),
        )

    def update(self) -> None:
        for obj in self.objects:
            obj.update()

    def draw(self) -> None:
        for obj in self.objects:
            obj.draw()
