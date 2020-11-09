import pygame #this module pygame has the functionality to build a game
from pygame.sprite import Group #this class behaves like a list with some extra functionality
from settings import Settings
from ship import Ship# This imports classes
from game_stats import GameStats
from button import Button
import game_functions as gf #This imports functions, so specification is needed
from scoreboard import Scoreboard 

def run_game():
	pygame.init()#Initialize background settings that pygame needs to work
	ai_settings = Settings()#this is an object based on the Settings class
	screen = pygame.display.set_mode((ai_settings.screen_width,
		ai_settings.screen_height))#this sets up the screen dimensions
	pygame.display.set_caption('ALIEN INVASION')#Set the caption

	play_button = Button(ai_settings, screen, "PLAY")
	#Make a ship

	ship = Ship(ai_settings, screen)
	bullets_group = Group()
	aliens_group = Group()
	gf.create_fleet(ai_settings, screen, ship, aliens_group)
	stats = GameStats(ai_settings)
	sb = Scoreboard(ai_settings, screen, stats)

	# Upload your own background music!
	music = pygame.mixer.music.load('ai_music.mp3')
	pygame.mixer.music.play(-1)


	while True:
		#Check for player input:

		gf.check_events(ai_settings, stats,  screen, play_button,
		 ship, bullets_group, aliens_group, sb)
		if stats.game_active:
		#Update ship position based on input etc.:
			ship.update_position()
			#create any new fired bullets based on input:
			gf.update_bullets(ai_settings, screen,
			 ship, aliens_group, bullets_group, stats, sb)
			#Use the updated positions and new bullets
			gf.update_aliens(ai_settings, stats,
			 screen, ship, aliens_group, bullets_group, sb)
			#to draw to the screen:
		gf.update_screen(ai_settings, screen, stats, ship,
		 aliens_group, bullets_group, play_button, sb)

run_game()
