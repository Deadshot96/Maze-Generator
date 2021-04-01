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