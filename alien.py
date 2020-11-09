import pygame 
from pygame.sprite import Sprite

alien_unflipped = pygame.image.load('images/alien.bmp')
alien_image = pygame.transform.flip(alien_unflipped, False, True)

class Alien(Sprite):
	def __init__(self, ai_settings, screen):
		super().__init__()
		self.screen = screen
		self.ai_settings = ai_settings
		self.image = alien_image

		#Rects:
		self.rect = self.image.get_rect()

		#Start near the top left corner
		#add space to the left equal to the width of the rect
		self.rect.x = self.rect.width 
		# add space to the top equal to the height of the rect
		self.rect.y = self.rect.height

		#store the alien's exact position
		self.x = float(self.rect.x)



	def check_edges(self):#return True if alien is at either edge of the screen
		screen_rect = self.screen.get_rect()
		if self.rect.right >= screen_rect.right:
			return True
		elif self.rect.left <= 0:
			return True
			

	def update(self):
		self.x += (self.ai_settings.alien_horizontal_speed
		 * self.ai_settings.fleet_direction) #multiplied by either 1 or -1, to move left or right
		self.rect.x = self.x

	def blitme(self):
		self.screen.blit(self.image, self.rect)

	

