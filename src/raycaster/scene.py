import pygame as pg

from .config import HALF_HEIGHT, SCENE_WIDTH, SCENE_X
from .minimap import MiniMap
from .player import Player
from .raycaster import Raycaster


class Scene:
    """Scene containing all game objects and rendering logic."""

    def __init__(self) -> None:
        self.surface = pg.display.get_surface()

        self.player = Player()
        self.raycaster = Raycaster(self.player)
        self.mini_map = MiniMap(self.player)
        self.objects: list = [self.player]

    def _draw_background(self) -> None:
        """Draw static sky/floor panels for the 3D viewport."""
        pg.draw.rect(
            self.surface,
            pg.Color("blue"),
            pg.Rect(
                SCENE_X,
                0,
                SCENE_WIDTH,
                HALF_HEIGHT,
            ),
        )

        pg.draw.rect(
            self.surface,
            pg.Color("brown"),
            pg.Rect(
                SCENE_X,
                HALF_HEIGHT,
                SCENE_WIDTH,
                HALF_HEIGHT,
            ),
        )

    def blank(self) -> None:
        """Refresh screen."""
        self.surface.fill(pg.Color("black"))
        self._draw_background()

    def update(self) -> None:
        """Update all dynamic scene objects."""
        for obj in self.objects:
            obj.update()

    def draw(self) -> None:
        """Draw everything in the scene."""
        self.raycaster.draw()
        self.mini_map.draw()
        for obj in self.objects:
            obj.draw()
