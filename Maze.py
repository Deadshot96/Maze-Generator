import random
import pygame
from Cell import Cell
from settings import *

class Maze:
    
    def __init__(self):
        self.width = WIDTH
        self.height = HEIGHT
        self.maze_width = MAZE_WIDTH
        self.maze_height = MAZE_HEIGHT
        self.xoff = XOFF
        self.yoff = YOFF
        self.fps = FPS
        self.size = SIZE
        self.rows = self.maze_height // self.size
        self.cols = self.maze_width // self.size
        self.font = None
        self.maze = None
        self.clock = None
        self.win = None
        self.maze_win = None
        self.offsets = ((0, -1), (1, 0), (0, 1), (-1, 0))

    def grid_init(self):
        self.maze = list()
        for row in range(self.rows):
            self.maze.append(list())
            for col in range(self.cols):
                self.maze[row].append(Cell(row, col, self.size))

    def is_valid_dims(self, row: int, col: int) -> bool:
        return row in range(self.rows) and col in range(self.cols)

    def update_neighbors(self):
        for row in self.maze:
            for cell in row:
                r, c = row.get_dims()

                for i, j in self.offsets:
                    newR = r + i
                    newC = c + j

                    if self.is_valid_dims(newR, newC):
                        newCell = self.maze[newR][newC]
                        cell.add_neighbor(newCell)

    def maze_init(self):
        pass

    def run(self):
        pass

if __name__ == "__main__":
    X = Maze()
    X.run()