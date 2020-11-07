import sys
import pygame

def run_game():
	pygame.init()
	screen = pygame.display.set_mode((1200,800))
	pygame.display.set_caption('BLUE SKY')
	bg_color = (27,195,237)

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
		screen.fill(bg_color)
		pygame.display.flip()

run_game()