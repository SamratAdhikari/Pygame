# Module
import pygame

# USe this all the time
pygame.init()

# Images
walkRight = [pygame.image.load('images/R1.png'), pygame.image.load('images/R2.png'),pygame.image.load('images/R3.png'),
			pygame.image.load('images/R4.png'), pygame.image.load('images/R5.png'), pygame.image.load('images/R6.png'),
			pygame.image.load('images/R7.png'), pygame.image.load('images/R8.png'),pygame.image.load('images/R9.png')]
walkLeft = [pygame.image.load('images/L1.png'), pygame.image.load('images/L2.png'), pygame.image.load('images/L3.png'), 
			pygame.image.load('images/L4.png'), pygame.image.load('images/L5.png'), pygame.image.load('images/L6.png'), 
			pygame.image.load('images/L7.png'), pygame.image.load('images/L8.png'),pygame.image.load('images/L9.png')]
bg = pygame.image.load('images/Background.jpg')
char = pygame.image.load('images/standing.png')

# Class for PLayer
class player(object):
	def __init__(self, x, y, width, height):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.velocity = 5
		# Player Variables
		self.isJump = False
		self.jumpCount = 10
		self.left = False
		self.right = False
		self.walkCount = 0
		self.standing = True

	def draw(self, win):
		if self.walkCount + 1 >= 27:
			self.walkCount = 0

		if not (self.standing):
			if self.left:
				win.blit(walkLeft[self.walkCount//3], (self.x, self.y))
				self.walkCount += 1

			elif self.right:
				win.blit(walkRight[self.walkCount//3], (self.x, self.y))
				self.walkCount += 1

		else:
			# win.blit(char, (self.x, self.y))
			if self.right:
				win.blit(walkRight[0], (self.x, self.y))
			elif self.left:
				win.blit(walkLeft[0], (self.x, self.y))


# Class for Projectiles
class project(object):
	def __init__(self, x, y, radius, color, facing):
		self.x = x
		self.y = y
		self.radius = radius
		self.color = color
		self.facing = facing 
		self.velocity = 8 * facing

	def draw(self, win):
		pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)


# Clas for Enemies
class enemy(object):
    walkRight = [pygame.image.load('images/R1E.png'), pygame.image.load('images/R2E.png'), pygame.image.load('images/R3E.png'), 
    			pygame.image.load('images/R4E.png'), pygame.image.load('images/R5E.png'), pygame.image.load('images/R6E.png'), 
    			pygame.image.load('images/R7E.png'), pygame.image.load('images/R8E.png'), pygame.image.load('images/R9E.png'), 
    			pygame.image.load('images/R10E.png'), pygame.image.load('images/R11E.png')]
    walkLeft = [pygame.image.load('images/L1E.png'), pygame.image.load('images/L2E.png'), pygame.image.load('images/L3E.png'), 
    			pygame.image.load('images/L4E.png'), pygame.image.load('images/L5E.png'), pygame.image.load('images/L6E.png'), 
    			pygame.image.load('images/L7E.png'), pygame.image.load('images/L8E.png'), pygame.image.load('images/L9E.png'), 
    			pygame.image.load('images/L10E.png'), pygame.image.load('images/L11E.png')]

    def __init__(self, x, y ,width, height, end):
    	self.x = x
    	self.y = y
    	self.width = width
    	self.height = height
    	self.end = end
    	self.walkCount = 0
    	self.path = [self.x, self.end]
    	self.velocity = 3

    def draw(self, win):
    	self.move()
    	if self.walkCount + 1 <= 33:
    		self.walkCount = 0

    	if velocity > 0:
    		win.blit(self.walkRight[self.walkCount//3], (self.x, self.y))
    		walkCount += 1

    	else:
    		win.blit(self.walkLeft[self.walkCount//3], (self.x, self.y))
    		walkCount += 1

    def move(self):
    	if self.velocity > 0:
    		if self.x + self.velocity < self.path[1]:
    			self.x += self.velocity
    		else:
    			self.velocity *= -1
    			self.walkCount = 0

    	else:
    		self.x - self.velocity > self.path[0]
    		self.x += self.velocity
    		self.velocity *= -1
    		self.walkCount = 0






# Game Variables
# Screen Geometry
WIDTH = 675
HEIGHT = 435

# # Geometry of our game object
# width = 64
# height = 64

# # Position on the window to place our game object
# x = 5
# y = HEIGHT - height - 60

# Clock Speed for FPS
clock = pygame.time.Clock()


# Create a Window of geometry("500x500")
win = pygame.display.set_mode((WIDTH, HEIGHT))
# Set Title to our Pygame Window
pygame.display.set_caption("Shooting Game")


# Function
def reDrawGameWindow():
	global walkCount

	win.blit(bg, (0, 0))
	# Draw the game object on the screen
	# pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
	# pygame.draw.rect(win, RED, (x, y, width, height))
	man.draw(win)

	for bullet in bullets:
		bullet.draw(win)

	# Update the display
	pygame.display.update()


# Game Loop
man = player(205, HEIGHT-64-15, 64, 64)
run = True
bullets = []
while run:
	# Set time to refresh 1000 = 1 sec
	clock.tick(27)

	# Key Binding/ Event Handling
	# When close button is clicked
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	for bullet in bullets:
		if bullet.x < WIDTH - 5 and bullet.x > 0:
			bullet.x += bullet.velocity
		else:
			bullets.pop(bullets.index(bullet))


	# Handling keys
	keys = pygame.key.get_pressed()

	# Arrow Keys
	if keys[pygame.K_SPACE]:
		if man.left:
			facing = -1
		else:
			facing = 1

		if len(bullets) < 5:
			bullets.append(project(round(man.x + man.width//2), round(man.y + man.height//2), 2, (0, 0, 0), facing))


	if keys[pygame.K_LEFT] and man.x > man.velocity:
		man.x -= man.velocity
		man.left = True
		man.right = False
		man.standing = False

	elif keys[pygame.K_RIGHT] and man.x < WIDTH - man.width - man.velocity:
		man.x += man.velocity
		man.right = True
		man.left = False
		man.standing = False

	else:
		# man.right = False
		# man.left = False
		man.walkCount = 0
		man.standing = True

	if not (man.isJump):
		if keys[pygame.K_UP]:
			man.isJump = True
			man.right = False
			man.left = False
			man.walkCount = 0

	else:
		if man.jumpCount >= -10:
			neg = 1
			if man.jumpCount < 0:
				neg = -1

			man.y -= (man.jumpCount ** 2) * 0.5 * neg
			man.jumpCount -= 1
		else:
			man.isJump = False
			man.jumpCount = 10

	reDrawGameWindow()

pygame.quit()