import sys
import pygame
from mario import Mario 
from mario_settings import *
import mario_functions as mf

def run_game():
	pygame.init()
	mario_settings = MarioSettings()
	screen = pygame.display.set_mode((mario_settings.screen_width,
		mario_settings.screen_height))
	pygame.display.set_caption('Mario')
	bg_color = mario_settings.bg_color
	mario = Mario(screen)

	pygame.key.set_repeat(10,7) #Continious movement function in pygame

	while True:
		mf.check_events(mario)
		mf.update_screen(mario_settings, screen, mario)

run_game()
