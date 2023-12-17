import pygame
import sys
import algorithm


class Block:
	def __init__(self, x, y, width, height, color=(128, 128, 128), id=None):
		self.x = x
		self.y = y
		self.pos = (x, y)
		self.width = width
		self.height = height
		self.size = (self.width, self.height)
		self.color = color
		self.id = id

	def draw(self, surface):
		pygame.draw.rect(surface, self.color, (self.pos, self.size))

	def isClicked(self):
		x, y = pygame.mouse.get_pos()
		if self.x < x < self.x + self.width and self.y < y < self.y + self.height:
			return True
		else:
			return False


class Button(Block):
	def __init__(self, text, text_size, text_font, x, y, width, height, color=(128, 128, 128), text_color=(0, 0, 0)):
		Block.__init__(self, x, y, width, height, color)
		self.text = text
		self.image = pygame.Surface([width, height])
		self.image.fill(color)
		self.font = pygame.font.SysFont(text_font, text_size, False, False)
		self.text_render = self.font.render(text, True, text_color)

	def draw(self, surface):
		w = (self.width / 2 - (self.text_render.get_width() / 2))
		h = (self.height / 2 - (self.text_render.get_height() / 2))
		self.image.blit(self.text_render, [w, h])
		surface.blit(self.image, (self.x, self.y))


class Label(Block):
	def __init__(self, text, text_size, text_font, x, y, width, height, color=(128, 128, 128), text_color=(0, 0, 0)):
		Block.__init__(self, x, y, width, height, color)
		self.text = text
		self.image = pygame.Surface([width, height])
		self.image.fill(color)
		self.font = pygame.font.SysFont(text_font, text_size, False, False)
		self.text_render = self.font.render(text, True, text_color)

	def draw(self, surface):
		w = (self.width / 2 - (self.text_render.get_width() / 2))
		h = (self.height / 2 - (self.text_render.get_height() / 2))
		self.image.blit(self.text_render, [w, h])
		surface.blit(self.image, (self.x, self.y))


def getNumberDisc():
	pygame.init()
	pygame.display.set_caption("Nhập số đĩa")
	editSize = (300, 200)
	editScreen = pygame.display.set_mode(size=editSize)
	n = 1
	buttonAdd = Button("+", 20, "Calibri", 200, 50, 40, 20)
	buttonMinus = Button("-", 20, "Calibri", 200, 90, 40, 20)
	buttonOk = Button("OK", 20, "Calibri", 100, 140, 100, 30)
	while True:
		showNumber = Label(f"{n}", 15, "Calibri", 80, 70, 60, 20)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				return n
			elif event.type == pygame.MOUSEBUTTONDOWN:
				if buttonOk.isClicked():
					pygame.quit()
					return n
				if buttonAdd.isClicked() and n < 12:
					n += 1
				elif buttonMinus.isClicked() and n > 3:
					n -= 1
		editScreen.fill((255, 255, 255))
		buttonAdd.draw(editScreen)
		buttonMinus.draw(editScreen)
		buttonOk.draw(editScreen)
		showNumber.draw(editScreen)
		pygame.display.update()

def drawDiscs(discs, screen, choose, f):
	for i in range(0, 3):
		for j in range(0, len(discs[i])):
			space = 30
			weight = 15
			w = DISC_WIDTH + weight * discs[i][j]
			if discs[i][j] % 2:
				color = (255, 0, 0)
			elif discs[i][j] % 3:
				color = (0, 255, 0)
			else:
				color = (0, 0, 255)
			if i == 0:
				if choose and f == i and len(discs[i]) - 1 == j:
					pygame.draw.rect(screen, color, [(WIDTH / 2 - 210 - w / 2, 110), (w, DISC_HEIGHT)])
				else:
					pygame.draw.rect(screen, color, [(WIDTH / 2 - 210 - w / 2, 500 - space * j), (w, DISC_HEIGHT)])
			if i == 1:
				if choose and f == i and len(discs[i]) - 1 == j:
					pygame.draw.rect(screen, color, [(WIDTH / 2 - w / 2, 110), (w, DISC_HEIGHT)])
				else:
					pygame.draw.rect(screen, color, [(WIDTH / 2 - w / 2, 500 - space * j), (w, DISC_HEIGHT)])
			if i == 2:
				if choose and f == i and len(discs[i]) - 1 == j:
					pygame.draw.rect(screen, color, [(WIDTH / 2 - w / 2 + 210, 110), (w, DISC_HEIGHT)])
				else:
					pygame.draw.rect(screen, color, [(WIDTH / 2 - w / 2 + 210, 500 - space * j), (w, DISC_HEIGHT)])

def move(f, t, discs):
	discs[t].append(discs[f].pop())

def save(steps, discs):
	steps.append([tuple(discs[0]), tuple(discs[1]), tuple(discs[2])])

if __name__ == "__main__":
	DISC_WIDTH = 40
	DISC_HEIGHT = 20
	n = getNumberDisc()
	mininum_step = 2 ** n - 1

	pygame.init()
	pygame.display.set_caption("Trò chơi tháp Hà Nội")
	WIDTH, HEIGHT = 900, 700
	screen = pygame.display.set_mode((WIDTH, HEIGHT))

	steps = []
	pointer = 0
	discs = [[i for i in range(n - 1, -1, -1)], [], []]
	save(steps, discs)
	f = None
	choose = False
	game_over = False

	objects = []

	t1 = Block(WIDTH / 2 - 100 - 210, HEIGHT / 2 - 250, 200, 500, id=0)
	t2 = Block(WIDTH / 2 - 100, HEIGHT / 2 - 250, 200, 500, id=1)
	t3 = Block(WIDTH / 2 - 100 + 210, HEIGHT / 2 - 250, 200, 500, id=2)
	p1 = Block(WIDTH / 2 - 220, HEIGHT / 2 - 200, 20, 400, (255, 128, 0))
	p2 = Block(WIDTH / 2 - 10, HEIGHT / 2 - 200, 20, 400, (255, 128, 0))
	p3 = Block(WIDTH / 2 + 200, HEIGHT / 2 - 200, 20, 400, (255, 128, 0))
	p4 = Block(WIDTH / 2 - 80 - 210, HEIGHT / 2 - 10 + 200, 160, 20, (255, 128, 0))
	p5 = Block(WIDTH / 2 - 80, HEIGHT / 2 - 10 + 200, 160, 20, (255, 128, 0))
	p6 = Block(WIDTH / 2 - 80 + 210, HEIGHT / 2 - 10 + 200, 160, 20, (255, 128, 0))
	btn_bo = Button("Bỏ đang chọn", 20, "Calibri", WIDTH / 2 - 60, HEIGHT / 2 + 280, 120, 30)
	objects = [t1, t2, t3, p1, p2, p3, p4, p5, p6, btn_bo]

	btn_playAgain = Button("Chơi lại", 20, "Calibri", WIDTH / 2 + 200, HEIGHT / 2 + 280, 120, 30, color=(255, 0, 0))
	btn_back = Button("Back", 20, "Calibri", WIDTH / 2 - 200, 50, 120, 30)
	btn_next = Button("Next", 20, "Calibri", WIDTH / 2 + 80, 50, 120, 30)
	endgame_objects = [btn_playAgain, btn_back, btn_next]

	btn_automatic = Button("Automatic", 20, "Calibri", WIDTH / 2 + 200, 50, 200, 30, color=(255, 0, 0))

	while True:
		screen.fill((255, 255, 255))
		if len(steps) == 1:
			btn_automatic.draw(screen)
		for object in objects:
			object.draw(screen)
		if not game_over:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
				if event.type == pygame.MOUSEBUTTONDOWN:
					if btn_bo.isClicked():
						choose = False
						f = None
					if btn_automatic.isClicked() and len(steps) == 1:
						number_disc = n
						Tower1 = ['A'] + discs[0]
						Tower2 = ['B']
						Tower3 = ['C']
						Towers = [Tower1, Tower2, Tower3]
						algorithm.Algorithm(number_disc, Tower1, Tower3, Tower2, Towers, steps)
						game_over = True
						pointer = len(steps) - 1
						discs = steps[pointer]
					if t1.isClicked() and discs[0] != [] and not choose:
						f = t1.id
						choose = True
					if t2.isClicked() and discs[1] != [] and not choose:
						f = t2.id
						choose = True
					if t3.isClicked() and discs[2] != [] and not choose:
						f = t3.id
						choose = True
					if t1.isClicked() and choose:
						if (discs[0] and discs[0][-1] > discs[f][-1]) or not discs[0]:
							move(f, t1.id, discs)
							save(steps, discs)
							choose = False
							f = None
					if t2.isClicked() and choose:
						if (discs[1] and discs[1][-1] > discs[f][-1]) or not discs[1]:
							move(f, t2.id, discs)
							save(steps, discs)
							choose = False
							f = None
					if t3.isClicked() and choose:
						if (discs[2] and discs[2][-1] > discs[f][-1]) or not discs[2]:
							move(f, t3.id, discs)
							save(steps, discs)
							choose = False
							f = None
		if not discs[0] and not discs[1]:
			game_over = True
			pointer = len(steps) - 1
		if game_over:
			choose = False
			for object in endgame_objects:
				object.draw(screen)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
				if event.type == pygame.MOUSEBUTTONDOWN:
					if btn_playAgain.isClicked():
						steps = []
						pointer = 0
						discs = [[i for i in range(n - 1, -1, -1)], [], []]
						save(steps, discs)
						f = None
						choose = False
						game_over = False
					if btn_back.isClicked() and pointer > 0:
						pointer -= 1
						discs = steps[pointer]
					if btn_next.isClicked() and pointer < len(steps) - 1:
						pointer += 1
						discs = steps[pointer]

		drawDiscs(discs, screen, choose, f)
		pygame.display.flip()
