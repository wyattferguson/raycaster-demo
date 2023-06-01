import pygame as pg

from config import *
from map import Map
from player import Player


class Game():

    def __init__(self) -> None:
        pg.init()
        pg.display.set_caption("Raycaster Demo")

        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode(SCREEN_SIZE)
        self.screen.fill(BLACK)
        self.running = True
        self.player = Player()
        self.board = Map(self.screen)

    def run(self):
        self.board.draw()
        while self.running:
            self.keyboard()
            self.update()

        pg.quit()

    def keyboard(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                self.running = False

    def update(self):
        pg.display.update()
        self.clock.tick(FPS)


if __name__ == "__main__":
    app = Game()
    app.run()
