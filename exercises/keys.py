import sys
import pygame

def run_game():
	pygame.init()
	screen = pygame.display.set_mode((800,800))
	pygame.display.set_caption('Keys')
	bg_color = (32,23,55)

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				print (event.key) #THAT'S PRETTY COOL!


		screen.fill(bg_color)
		pygame.display.flip()

run_game()