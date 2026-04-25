import pygame as pg

from .config import FPS, SCREEN_SIZE
from .scene import Scene


class Game:
    """Main game loop."""

    def __init__(self) -> None:
        pg.init()
        pg.display.set_caption("Raycaster Demo")
        pg.display.set_mode(SCREEN_SIZE)

        self.clock = pg.time.Clock()
        self.running = True
        self.scene = Scene()

    def _process_events(self) -> None:
        """Handle close and quit-related key events."""
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                self.running = False

    def run(self) -> None:
        """Run the game loop until a quit event occurs."""
        while self.running:
            self.scene.blank()
            self._process_events()
            self.scene.update()
            self.scene.draw()
            pg.display.update()
            self.clock.tick(FPS)

        pg.quit()


def main() -> None:
    """Start raycaster demo."""
    game = Game()
    game.run()


if __name__ == "__main__":
    main()
