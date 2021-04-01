import random
import pygame
from settings import *

class Cell:

    def __init__(self, row: int, col: int, size: int):
        self.row = row
        self.col = col
        self.size = size
        self.x = self.col * self.size
        self.y = self.row * self.size
        self.color = PURPLE
        self.wallColor = WHITE
        self.wallFlags = [True] * 4
        self.wallDict = ["top", "right", "bottom", "left"]
        self.visited = False
        self.neighbors = list()

    def is_visited(self):
        return self.visited

    def visit(self):
        self.visited = True

    def get_row(self):
        return self.row

    def get_col(self):
        return self.col

    def get_dims(self):
        return self.row, self.col

    def add_neighbor(self, cell):
        self.neighbors.append(cell)

    def get_neighbor_count(self):
        return len(self.neighbors)

    def get_neighbor(self):
        cell = None
        random.shuffle(self.neighbors)

        for spot in self.neighbors:
            if not spot.is_visited():
                cell = spot
                break

        return cell

    def draw(self, win: pygame.Surface):
        pass
