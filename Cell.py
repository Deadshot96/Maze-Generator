import random
import pygame
from settings import *
from typing import Tuple

class Cell:

    def __init__(self, row: int, col: int, size: int):
        self.row = row
        self.col = col
        self.size = size
        self.x = self.col * self.size
        self.y = self.row * self.size
        self.color = PURPLE
        self.wallColor = WHITE
        self.highLightColor = BLUE
        self.wallFlags = [True] * 4
        self.wallDict = ["top", "right", "bottom", "left"]
        self.visited = False
        self.neighbors = list()

    def is_visited(self) -> bool:
        return self.visited

    def visit(self) -> None:
        self.visited = True

    def get_row(self) -> int:
        return self.row

    def get_col(self) -> int:
        return self.col

    def get_dims(self) -> Tuple[int]:
        return self.row, self.col

    def add_neighbor(self, cell) -> None:
        self.neighbors.append(cell)

    def get_neighbor_count(self) -> int:
        return len(self.neighbors)

    def get_neighbor(self):
        cell = None
        random.shuffle(self.neighbors)

        for spot in self.neighbors:
            if not spot.is_visited():
                cell = spot
                break

        return cell

    def draw(self, win: pygame.Surface) -> None:
        if self.is_visited():
            pygame.draw.rect(win, self.color, (self.x, self.y, self.size, self.size), 0)

        if self.wallFlags[self.wallDict.index("top")]:
            pygame.draw.line(win, self.wallColor, (self.x, self.y), (self.x, self.y + self.size), 2)
        
        if self.wallFlags[self.wallDict.index("right")]:
            pygame.draw.line(win, self.wallColor, (self.x + self.size, self.y), (self.x + self.size, self.y + self.size), 2)
        
        if self.wallFlags[self.wallDict.index("bottom")]:
            pygame.draw.line(win, self.wallColor, (self.x, self.y + self.size), (self.x + self.size, self.y + self.size), 2)

        if self.wallFlags[self.wallDict.index("left")]:
            pygame.draw.line(win, self.wallColor, (self.x, self.y), (self.x, self.y + self.size), 2)

    def remove_wall(self, wall) -> None:
        if wall in self.wallDict:
            self.wallFlags[self.wallDict.index(wall)] = False

    def highlight(self, win: pygame.Surface) -> None:
        pygame.draw.rect(win, self.highLightColor, (self.x, self.y, self.size, self.size))
        pygame.display.update()
    