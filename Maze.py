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
        self.currentCell = None
        self.stack = list()
        self.offsets = ((0, -1), (1, 0), (0, 1), (-1, 0))

        self.maze_init()

    def grid_init(self) -> None:
        self.maze = list()
        for row in range(self.rows):
            self.maze.append(list())
            for col in range(self.cols):
                self.maze[row].append(Cell(row, col, self.size))

        self.update_neighbors()
        self.stack.clear()
        row, col = random.randrange(self.rows), random.randrange(self.cols)
        self.currentCell = self.maze[row][col]


    def is_valid_dims(self, row: int, col: int) -> bool:
        return row in range(self.rows) and col in range(self.cols)

    def update_neighbors(self) -> None:
        for row in self.maze:
            for cell in row:
                r, c = cell.get_dims()
                for i, j in self.offsets:
                    newR = r + i
                    newC = c + j

                    if self.is_valid_dims(newR, newC):
                        newCell = self.maze[newR][newC]
                        cell.add_neighbor(newCell)

    def maze_init(self):
        pygame.init()
        pygame.font.init()

        self.grid_init()

        self.win = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Maze Generator Developer")

        self.maze_win = self.win.subsurface((self.xoff, self.yoff, self.maze_width, self.maze_height))

        self.win.fill(YELLOW)
        self.maze_win.fill(BLACK)

        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont(FONT, FONT_SIZE)

        title = self.font.render(TITLE_TEXT, 1, RED)
        titleWidth, titleHeight = title.get_size()
        blitPoint = (self.width - titleWidth) // 2, (self.yoff - titleHeight) // 2

        self.win.blit(title, blitPoint)
        pygame.display.update()

    def quit(self):
        pygame.font.quit()
        pygame.quit()

    def draw(self):
        for row in self.maze:
            for cell in row:
                cell.draw(self.maze_win)

        pygame.display.update()

    def remove_wall(self, current, neighbor):
        rowDiff = current.get_row() - neighbor.get_row()
        colDiff = current.get_col() - neighbor.get_col()
        
        if rowDiff == 1:
            current.remove_wall('top')
            neighbor.remove_wall('bottom')
        elif rowDiff == -1:
            current.remove_wall('bottom')
            neighbor.remove_wall('top')
        elif colDiff == 1:
            current.remove_wall('left')
            neighbor.remove_wall('right')
        elif colDiff == -1:
            current.remove_wall('right')
            neighbor.remove_wall('left')


    def generate_maze(self):
        run = True
        
        while run:
            self.clock.tick(self.fps)
            self.draw()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.run()

            self.currentCell.visit()
            self.currentCell.highlight(self.maze_win)

            cell = self.currentCell.get_neighbor()

            if cell is None:
                if len(self.stack) != 0:
                    self.currentCell = self.stack.pop()
                else:
                    run = False
            else:
                self.stack.append(self.currentCell)   
                self.stack.append(cell)
                self.remove_wall(self.currentCell, cell)
                self.currentCell = cell


    def run(self):

        run = True
        while run:
            self.clock.tick(self.fps)
            self.draw()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.maze_win.fill(BLACK)
                        self.grid_init()

                    if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                        self.generate_maze()

        self.quit()

if __name__ == "__main__":
    X = Maze()
    X.run()