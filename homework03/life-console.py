import curses
import curses.ascii
import pathlib
from time import sleep

from life import GameOfLife
from ui import UI


class Console(UI):
    def __init__(self, life: GameOfLife) -> None:
        super().__init__(life)

    def draw_borders(self, screen) -> None:
        """ Отобразить рамку. """
        
        screen.clear()

    def draw_grid(self, screen) -> None:
        """ Отобразить состояние клеток. """

        for i in range(self.life.rows):
            for j in range(self.life.cols):
                if self.life.curr_generation[i][j] == 1:
                    screen.addch(i + 1, j + 1, "*")
                else:
                    screen.addch(i + 1, j + 1, " ")

    def run(self) -> None:
        screen = curses.initscr()
        curses.wrapper(self.draw_borders)
        while not self.life.is_max_generations_exceeded and self.life.is_changing:
            self.life.step()
            self.draw_borders(screen)
        curses.endwin()


if __name__ == "__main__":
    life = GameOfLife((24, 80), max_generations=50)
    gui = Console(life)
    gui.run()
