from config import GRID_COLS, GRID_ROWS, WINDOW_WIDTH, WINDOW_HEIGHT, GREY, WHITE, BLACK, ORANGE, TURQUOISE, RED, GREEN, PURPLE


class Cell:
    def __init__(self, row, col, width, height):
        self.row = row
        self.col = col
        self.x = col * width
        self.y = row * height
        self.width = width
        self.height = height
        self.color = WHITE
        self.neighbors = []
        self.g_score = float('inf')
        self.f_score = float('inf')
        self.distance = float('inf')

    def get_pos(self):
        return self.row, self.col

    def is_wall(self):
        return self.color == BLACK

    def is_start(self):
        return self.color == ORANGE

    def is_end(self):
        return self.color == TURQUOISE

    def reset(self):
        self.color = WHITE
        self.g_score = float('inf')
        self.f_score = float('inf')
        self.distance = float('inf')
        self.neighbors = []

    def make_start(self):
        self.color = ORANGE

    def make_end(self):
        self.color = TURQUOISE

    def make_wall(self):
        self.color = BLACK

    def make_visited(self):
        self.color = RED

    def make_frontier(self):
        self.color = PURPLE

    def make_path(self):
        self.color = GREEN

    def draw(self, win):
        import pygame
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))
        pygame.draw.rect(win, GREY, (self.x, self.y, self.width, self.height), 1)


class Grid:
    def __init__(self, cols=GRID_COLS, rows=GRID_ROWS, width=WINDOW_WIDTH, height=WINDOW_HEIGHT):
        self.cols = cols
        self.rows = rows
        self.width = width - 200  # reserve sidebar
        self.height = height
        self.cell_width = self.width // cols
        self.cell_height = self.height // rows
        self.grid = [[Cell(r, c, self.cell_width, self.cell_height) for c in range(cols)] for r in range(rows)]

    def draw(self, win):
        for row in self.grid:
            for cell in row:
                cell.draw(win)

    def get_cell(self, row, col):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            return self.grid[row][col]
        return None

    def reset_visited(self):
        for row in self.grid:
            for cell in row:
                if cell.color in (RED, PURPLE, GREEN):
                    cell.color = WHITE
                cell.g_score = float('inf')
                cell.f_score = float('inf')
                cell.distance = float('inf')

    def reset_all(self):
        for row in self.grid:
            for cell in row:
                cell.reset()

    def update_all_neighbors(self):
        for r in range(self.rows):
            for c in range(self.cols):
                cell = self.grid[r][c]
                cell.neighbors = []
                # up
                if r - 1 >= 0 and not self.grid[r - 1][c].is_wall():
                    cell.neighbors.append(self.grid[r - 1][c])
                # down
                if r + 1 < self.rows and not self.grid[r + 1][c].is_wall():
                    cell.neighbors.append(self.grid[r + 1][c])
                # left
                if c - 1 >= 0 and not self.grid[r][c - 1].is_wall():
                    cell.neighbors.append(self.grid[r][c - 1])
                # right
                if c + 1 < self.cols and not self.grid[r][c + 1].is_wall():
                    cell.neighbors.append(self.grid[r][c + 1])
