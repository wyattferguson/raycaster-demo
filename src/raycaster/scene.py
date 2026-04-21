import pygame as pg

from raycaster.config import HALF_HEIGHT, SCENE_WIDTH, SCENE_X
from raycaster.minimap import MiniMap
from raycaster.player import Player


class Scene:
    """Scene containing all game objects and rendering logic."""

    def __init__(self) -> None:
        self.surface = pg.display.get_surface()
        self.mini_map = MiniMap()
        self.objects: list[Player] = [Player()]

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
        self.mini_map.draw()
        self._draw_background()

    def update(self) -> None:
        """Update all dynamic scene objects."""
        for obj in self.objects:
            obj.update()

    def draw(self) -> None:
        """Draw all dynamic scene objects."""
        for obj in self.objects:
            obj.draw()
