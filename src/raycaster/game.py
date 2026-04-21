import pygame as pg

from raycaster.config import FPS, SCREEN_SIZE
from raycaster.scene import Scene


class Game:
    """Main game loop."""

    def __init__(self) -> None:
        pg.init()
        pg.display.set_caption("Wolf3D Game")

        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode(SCREEN_SIZE)

        self.running = True
        self.scene = Scene(self.screen)

    def update(self) -> None:
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                self.running = False

    def run(self) -> None:
        while self.running:
            self.scene.blank()
            self.update()
            self.scene.update()
            self.scene.draw()
            pg.display.update()
            self.clock.tick(FPS)

        pg.quit()


if __name__ == "__main__":
    app = Game()
    app.run()
