import sys
import pygame
from mario import *
# from mario_settings import *

def check_events(mario):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				mario.rect.bottom -= 10
			elif event.key == pygame.K_DOWN:
				mario.rect.bottom += 10
			elif event.key == pygame.K_RIGHT:
				mario.rect.centerx += 10
			elif event.key == pygame.K_LEFT:
				mario.rect.centerx -= 10


def update_screen(settings, screen, mario):
	screen.fill(settings.bg_color)
	mario.blitme()
	pygame.display.flip()