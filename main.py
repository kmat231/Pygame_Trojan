import pygame
import random
import math

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
walkRight = [pygame.image.load('R1.png'),pygame.image.load('R2.png'),pygame.image.load('R3.png'),pygame.image.load('R4.png'),pygame.image.load('R5.png'),pygame.image.load('R6.png'),pygame.image.load('R7.png'),pygame.image.load('R8.png'),pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'),pygame.image.load('L2.png'),pygame.image.load('L3.png'),pygame.image.load('L4.png'),pygame.image.load('L5.png'),pygame.image.load('L6.png'),pygame.image.load('L7.png'),pygame.image.load('L8.png'),pygame.image.load('L9.png')]
char = pygame.image.load('standing.png')
# Resize Character Sprite
walkLeft = [pygame.transform.smoothscale(i,(128,128)) for i in walkLeft]
walkRight = [pygame.transform.smoothscale(i,(128,128)) for i in walkRight]
char = pygame.transform.smoothscale(char,(128,128))

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
        if self.walkCount + 1 >= 27:
            self.walkCount = 0
        if self.left:
            screen.blit(walkLeft[self.walkCount // 3], (self.x, self.y))
        elif self.right:
            screen.blit(walkRight[self.walkCount // 3], (self.x, self.y))
        else:
            screen.blit(char, (self.x, self.y))

def redrawGameWindow():
    screen.blit(background,(0,0))
    person.draw(screen)
    pygame.display.update()



# Game Loop
person = hero(200,410, 64, 64)
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
    elif key_press[pygame.K_RIGHT] and person.x < 1200 - person.width:
        person.x += person.vel
        person.left  = False
        person.right = True
    else:
        person.right = False
        person.left  = False
        person.walkCount = 0

    if not (person.isJump):
        if key_press[pygame.K_DOWN] and person.y < 1200 - person.height:
            person.y += person.vel  #Vertical fire
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
pygame.quit()