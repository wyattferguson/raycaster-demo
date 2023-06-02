import pygame as pg

from board import Board
from config import *
from player import Player


class Game():

    def __init__(self) -> None:
        pg.init()
        pg.display.set_caption("Raycaster Demo")

        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode(SCREEN_SIZE)
        self.screen.fill(BLACK)
        self.running = True
        self.player = Player(self.screen)
        self.board = Board(self.screen)

    def run(self):

        while self.running:
            self.board.blank()
            self.board.draw()
            self.keyboard()
            self.player.draw()
            self.update()

        pg.quit()

    def keyboard(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                self.running = False
            elif event.type == pg.KEYDOWN:
                if event.key==pg.K_w:
                    self.player.move(UP)
                elif event.key==pg.K_a:
                    self.player.move(LEFT)
                elif event.key==pg.K_d:
                    self.player.move(RIGHT)
                elif event.key==pg.K_s:
                    self.player.move(DOWN)


    def update(self):
        pg.display.update()
        self.clock.tick(FPS)


if __name__ == "__main__":
    app = Game()
    app.run()
