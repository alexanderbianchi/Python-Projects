import pygame
import math
from queue import PriorityQueue


RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 255, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165 ,0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)

class node:
	def __init__(self,row,col,width,totalRows):
		self.row=row
		self.col = col
		self.x=row*width
		self.y=col*width
		self.color = WHITE
		self.neaighbors=[]
		self.width=width
		self.totalRows = totalRows
	def getPos(self):
		return self.row, self.col
	def isClosed(self):
		return self.color==RED
	def is_open(self):
		return self.color==GREEN
	def isBarrier(self):
		return self.color == BLACK
	def isEnd(self):
		return self.color == TURQUOISE
	def makeClosed(self):
		self.color = RED
	def makeOpen(self):
		self.color=GREEN
	def makeBarrier(self):
		self.color=BLACK
	def draw(self, win):
		pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))
	def makePath(self):
		self.color=PURPLE
	def makeStart(self):
		self.color = ORANGE
	def makeEnd(self):
		self.color=TURQUOISE
	def reset(self):
		self.color=WHITE
	def updateNeighbors(self, grid):
		self.neighbors = []
		if self.row < self.totalRows - 1 and not grid[self.row + 1][self.col].isBarrier(): # DOWN
			self.neighbors.append(grid[self.row + 1][self.col])

		if self.row > 0 and not grid[self.row - 1][self.col].isBarrier(): # UP
			self.neighbors.append(grid[self.row - 1][self.col])

		if self.col < self.totalRows - 1 and not grid[self.row][self.col + 1].isBarrier(): # RIGHT
			self.neighbors.append(grid[self.row][self.col + 1])

		if self.col > 0 and not grid[self.row][self.col - 1].isBarrier(): # LEFT
			self.neighbors.append(grid[self.row][self.col - 1])
	def __lt__(self,other):
		return False

def h(p1,p2):
	x1, y1 = p1
	x2,y2 = p2
	return abs(x1-x2)+abs(y1-y2)

def reconstructPath(cameFrom,current,draw):
	while current in cameFrom:
		current = cameFrom[current]
		current.makePath()
		draw()


def algorithm(draw,grid,start,end):
	count= 0 
	openSet = PriorityQueue()
	openSet.put((0,count,start))
	cameFrom = {}
	gScore= {node: float("inf") for row in grid for node in row}
	gScore[start] = 0
	fScore= {node: float("inf") for row in grid for node in row}
	fScore[start] = h(start.getPos(), end.getPos())

	openSetHash = {start}
	while not openSet.empty():
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()

		current = openSet.get()[2]
		openSetHash.remove(current)

		if current == end:
			reconstructPath(cameFrom,end,draw)
			end.makeEnd()
			start.makeStart()
			return True

		for neighbor in current.neighbors:
			tempGScore = gScore[current] + 1
			if tempGScore<gScore[neighbor]:
				cameFrom[neighbor] = current
				gScore[neighbor] = tempGScore
				fScore[neighbor] = tempGScore+h(neighbor.getPos(),end.getPos())
				if neighbor not in openSetHash:
					count += 1
					openSet.put((fScore[neighbor],count,neighbor))
					openSetHash.add(neighbor)
					neighbor.makeOpen()
		draw()

		if current != start:
			current.makeClosed()
	return False
 
def drawGrid(win,rows,width):
	gap = width // rows
	for i in range(rows):
		pygame.draw.line(win, GREY, (0, i * gap), (width, i * gap))
		for j in range(rows):
			pygame.draw.line(win, GREY, (j * gap, 0), (j * gap, width))

def draw(win,grid,rows,width):
	win.fill(WHITE)

	for row in grid:
		for node in row:
			node.draw(win)

	drawGrid(win, rows, width)
	pygame.display.update()


def getClickedPosition(pos,rows,width):
	gap = width //rows
	y,x = pos

	row = y//gap
	col=x//gap
	return row,col

def makeGrid(rows,width):
	grid = []
	gap = width // rows
	for i in range(rows):
		grid.append([])
		for j in range(rows):
			Node = node(i, j, gap, rows)
			grid[i].append(Node)

	return grid

def main(win,width):
	rows = 50
	grid = makeGrid(rows,width)
	start = None
	end= None

	run=True 
	started= False

	while run:
		draw(win,grid,rows,width)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run=False
			if started:
				continue

			if pygame.mouse.get_pressed()[0]:
				pos= pygame.mouse.get_pos()
				row,col = getClickedPosition(pos,rows,width)
				node= grid[row][col]
				if not start and node != end:
					start = node
					start.makeStart()
				elif not end and node !=start:
					end= node
					node.makeEnd()

				elif node != end and node != start:
					node.makeBarrier()


			elif pygame.mouse.get_pressed()[2]:
				pos= pygame.mouse.get_pos()
				row,col = getClickedPosition(pos,rows,width)
				node= grid[row][col]
				node.reset()
				if node == end:
					end = None
				if node == start:
					start = None

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE and start and end:
					for row in grid:
						for spot in row:
							spot.updateNeighbors(grid)
					algorithm(lambda: draw(win,grid,rows,width),grid,start,end)

				if event.key == pygame.K_c:
					start=None
					end=None
					grid=makeGrid(rows,width)
	pygame.quit()


WIDTH = 800
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("A* Path Finding Algorithm")


main(WIN, WIDTH)