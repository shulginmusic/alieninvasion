import pygame
from pygame.sprite import Sprite

#A class to manage bullets fired from the ship
class Bullet(Sprite):
	def __init__(self, ai_settings, screen, ship):#Create a bullet
		super().__init__()#Properly inherit from Sprite class
		self.screen = screen
		#Create a bullet rect at (0,0) and then set correct position
		self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
			ai_settings.bullet_height)
		#Position of bullet, same as ship
		self.rect.centerx = ship.rect.centerx
		self.rect.top = ship.rect.top
		#Store the bullet's y-axis position as decimal value
		self.y = float(self.rect.y)

		self.color = ai_settings.bullet_color
		self.speed_factor = ai_settings.bullet_speed_factor

	def update(self):#move the bullet up the screen
		#Update the decimal position of the bullet
		self.y -= self.speed_factor
		#Update the bullet's rect position
		self.rect.y = self.y

	def draw_bullet(self):#draw the bullet to the screen
		pygame.draw.rect(self.screen, self.color, self.rect)





