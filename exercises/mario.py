import pygame

class Mario():
	def __init__(self,screen):
		self.screen = screen
		self.image = pygame.image.load('mario.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = self.screen.get_rect()

		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.centerx

	def blitme(self):
		self.screen.blit(self.image, self.rect)

