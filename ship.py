import pygame
from pygame.sprite import Sprite
from settings import Settings

class Ship(Sprite):
	def __init__(self, ai_settings, screen):
		super().__init__()
		#Initialize the ship and set its
		#starting position
		self.screen = screen
		self.ai_settings = ai_settings
		#Load the ship and get its rect
		self.image = pygame.image.load('images/ship.bmp')
		#this function returns a surface representing a ship, which
		#is then store in self.image
		self.rect = self.image.get_rect()#Accesses the ship's rect attr
		#-bute, the rectange that is around the ship, so it's easier
		#to work with
		self.screen_rect = screen.get_rect()
		#Start each new ship at the bottom of the screen
		self.rect.centerx = self.screen_rect.centerx #x-coordinate
		self.rect.bottom = self.screen_rect.bottom #y-coordinate

		#Movement flags
		self.moving_right = False
		self.moving_left = False

		#Store a decimal value for the ship's center, since rect
		#attributes only store integers

		self.center = float(self.rect.centerx) #decimals

	def update_position(self):
		#self.rect.right = the right edge of the ship's rectangle
		#0 is the left edge of the x axis of the ship, the rect of the ship
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.center += self.ai_settings.ship_speed_factor

		if self.moving_left and self.rect.left > 0: #If this was elif if would have priority
			self.center -= self.ai_settings.ship_speed_factor
			
		self.rect.centerx = self.center #decimals

	def blitme(self):#Draw the ship at its current location
		self.screen.blit(self.image, self.rect)

	def center_ship(self):
		#Center the ship on the screen
		self.center = self.screen_rect.centerx
















