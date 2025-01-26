import pygame as pg

from config import FPS, SCREEN_SIZE
from scene import Scene


class Game:
	def __init__(self) -> None:
		pg.init()
		pg.display.set_caption("Wolf3D Game")

		self.clock = pg.time.Clock()
		self.screen = pg.display.set_mode(SCREEN_SIZE)

		self.running = True
		self.scene = Scene(self.screen)

	def run(self):
		while self.running:
			self.scene.blank()
			self.update()
			self.scene.update()
			self.scene.draw()
			pg.display.update()
			self.clock.tick(FPS)

		pg.quit()

	def update(self):
		for event in pg.event.get():
			if event.type == pg.QUIT or event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
				self.running = False


if __name__ == "__main__":
	app = Game()
	app.run()
