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
        

    def run(self):
        pass

if __name__ == "__main__":
    X = Maze()
    X.run()