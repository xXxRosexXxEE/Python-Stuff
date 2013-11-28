import pygame, sys
from pygame.locals import *
from random import *

pygame.init()

windowSurface = pygame.display.set_mode((640, 480), 0, 32)
pygame.display.set_caption('Pixel Spam')

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255,255,0)

basicFont = pygame.font.SysFont(None, 48)
basicFont.set_bold(True)

RandomPixels = basicFont.render('Random Pixels', True, WHITE,YELLOW)

textRect = RandomPixels.get_rect()
textRect.centerx = windowSurface.get_rect().centerx
textRect.centery = windowSurface.get_rect().centery

a = 1
w = 0

while True:
	windowSurface.fill(BLACK)
	for  w  in  range (randint(0,1000),randint(1,1000)):		
		pixArray = pygame.PixelArray(windowSurface)	
		pixArray[a*w][a]  = YELLOW
		del pixArray
		windowSurface.blit(RandomPixels, textRect)
		pygame.display.update()
		for event in pygame.event.get():
			if event.type == QUIT:
					pygame.quit()
					sys.exit()
