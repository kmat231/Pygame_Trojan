import pygame
import random
import math
from SystemInfo import *

# initalize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((1200,800))

#background
image = pygame.image.load('2959.png')
background = pygame.transform.scale(image, (1200, 800))

# Title and Icon
pygame.display.set_caption("Cyber War")

# Character Sprite Image
walkRight = [pygame.image.load('Ironman/R (1).png'),pygame.image.load('Ironman/R (2).png'),pygame.image.load('Ironman/R (3).png'),pygame.image.load('Ironman/R (4).png'),pygame.image.load('Ironman/R (5).png'),pygame.image.load('Ironman/R (6).png'),pygame.image.load('Ironman/R (7).png'),pygame.image.load('Ironman/R (8).png'),pygame.image.load('Ironman/R (9).png'), pygame.image.load('Ironman/R (10).png')]
walkLeft = [pygame.image.load('Ironman/L (1).png'),pygame.image.load('Ironman/L (2).png'),pygame.image.load('Ironman/L (3).png'),pygame.image.load('Ironman/L (4).png'),pygame.image.load('Ironman/L (5).png'),pygame.image.load('Ironman/L (6).png'),pygame.image.load('Ironman/L (7).png'),pygame.image.load('Ironman/L (8).png'),pygame.image.load('Ironman/L (9).png'),pygame.image.load('Ironman/L (10).png')]
char = pygame.image.load('Ironman/standing.png')
# Resize Character Sprite
# walkLeft = [pygame.transform.smoothscale(i,(128,128)) for i in walkLeft]
# walkRight = [pygame.transform.smoothscale(i,(128,128)) for i in walkRight]
# char = pygame.transform.smoothscale(char,(128,128))

clock = pygame.time.Clock()
class hero(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.left = False
        self.right = False
        self.walkCount = 0
        self.jumpCount = 10

    def draw(self, screen):
        if self.walkCount + 1 >= 30:
            self.walkCount = 0
        if self.left:
            screen.blit(walkLeft[int(self.walkCount // 3)], (int(self.x), int(self.y)))
        elif self.right:
            screen.blit(walkRight[int(self.walkCount // 3)], (int(self.x), int(self.y)))
        else:
            screen.blit(char, (int(self.x), int(self.y)))
class blast(object):
    def __init__(self, x, y, radius, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.facing = facing
        self.vel = 8 * facing
    def draw(self, right, left, screen):
        if right:
            bullet = pygame.image.load('Ironman/blastR.png')
        else:
            bullet = pygame.image.load('Ironman/blastR.png')



def redrawGameWindow():
    screen.blit(background,(0,0))
    person.draw(screen)
    pygame.display.update()



# Game Loop
person = hero(200,600, 100, 120)
blast = []
running = True
while running:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Proper key is pressed
    key_press = pygame.key.get_pressed()

    if key_press[pygame.K_LEFT] and person.x > person.vel:
        person.x -= person.vel
        person.left = True
        person.right = False
        person.walkCount += 1
    elif key_press[pygame.K_RIGHT] and person.x < 1200 - person.width:
        person.x += person.vel
        person.left  = False
        person.right = True
        person.walkCount += 1
    else:
        person.right = False
        person.left = False
        person.walkCount = 0

    if not (person.isJump):
        if key_press[pygame.K_UP] and person.y > person.vel:
            person.isJump = True
            person.right = False
            person.left  = False
            person.walkCount = 0
    else:
        if person.jumpCount >= -10:
            neg = 1
            if person.jumpCount < 0:
                neg = -1
            person.y -= (person.jumpCount ** 2) * 0.5 * neg
            person.jumpCount -= 1
        else:
            person.isJump = False
            person.jumpCount = 10

    redrawGameWindow()
RunSystemScan()
pygame.quit()