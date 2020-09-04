import pygame
import math
from queue import PriorityQueue

WIDTH = 600


# COLORS=[(255, 255, 255), # "WHITE" =
#     (255, 255, 0),# "YELLOW" =
#     (128, 128, 128),# "GREY" =
#     (0, 0, 0),# "BLACK" =
#     (255, 0, 0), #"RED" =
#     (0, 255, 0),# "GREEN" =
#     (0, 255, 0), #"BLUE" =
#     (128, 0, 128), #"PURPLE" =
#     (255, 165 ,0) ,#"ORANGE" =
#     (64, 224, 208)# "TURQUOISE" =
#     ]
COLORS=[(255, 255, 255),(255, 255, 0),(128, 128, 128),(0, 0, 0),(255, 0, 0),(0, 255, 0),(0, 255, 0),(128, 0, 128),(255, 165 ,0),(64, 224, 208)]

class Spot:
	def __init__(self, row, col, width, total_rows,state):
        # self.state=state
		self.row = row
		self.state = state
		self.col = col
		self.x = row * width
		self.y = col * width
		self.color = COLORS[self.state]
		self.neighbors = []
		self.width = width
		self.total_rows = total_rows
		self.parent=None

	def get_pos(self):
		return self.row, self.col

	def get_state(self):
		return self.state

	def put_state(self,x):
		self.state=x
		self.color=COLORS[x]

	def draw(self, win):
		pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

	def update_neighbors(self, grid):
		self.neighbors = []
		if self.row < self.total_rows - 1 and grid[self.row + 1][self.col].get_state()!=3: # DOWN
			self.neighbors.append(grid[self.row + 1][self.col])

		if self.col < self.total_rows - 1 and grid[self.row][self.col+1].get_state()!=3: # RIGHT
			self.neighbors.append(grid[self.row][self.col + 1])

		if self.row > 0 and grid[self.row - 1][self.col].get_state()!=3: # UP
			self.neighbors.append(grid[self.row - 1][self.col])

		if self.col > 0 and grid[self.row][self.col-1].get_state()!=3: # LEFT
			self.neighbors.append(grid[self.row][self.col - 1])

	def __lt__(self, other):
		return False

def make_grid(rows, width):
	grid = []
	gap = width // rows
	for i in range(rows):
		grid.append([])
		for j in range(rows):
			spot = Spot(i, j, gap, rows,0)
			grid[i].append(spot)

	return grid


def draw_grid(win, rows, width):
	gap = width // rows
	for i in range(rows):
		pygame.draw.line(win, COLORS[2], (0, i * gap), (width, i * gap))
		for j in range(rows):
			pygame.draw.line(win, COLORS[2], (j * gap, 0), (j * gap, width))


def draw(win, grid, rows, width):
	for row in grid:
		for spot in row:
			spot.draw(win)

	draw_grid(win, rows, width)
	pygame.display.update()


def get_clicked_pos(pos, rows, width):
	gap = width // rows
	y, x = pos

	row = y // gap
	col = x // gap

	return row, col
