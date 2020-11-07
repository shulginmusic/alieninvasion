import pygame.font

class Button():
	def __init__(self, ai_settings, screen, msg):
		#Initialize button attributes
		self.screen = screen
		self.screen_rect = self.screen.get_rect()

		#Set button dimensions and properties
		self.width, self.height = 200, 50
		self.button_color = (0, 255, 0)
		self.text_color = (255, 255, 255)
		self.font = pygame.font.SysFont(None, 48) #None = Default font
		#Build the button's rect object and center it
		self.rect = pygame.Rect(0, 0, self.width, self.height)
		self.rect.center = self.screen_rect.center

		#The button message needs to be prepped only once
		self.prep_msg(msg)#Pygame needs a message to display text, text is displayed as an image

	def prep_msg(self, msg):
		#Turn msg into a rendered image and center text on the button
		self.msg_image = self.font.render(msg, True, #Boolean turns antialiasing on/off, makes text smoother on the edges
		 self.text_color, self.button_color)
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect.center = self.screen_rect.center

	def draw_button(self):
		#Draw blank button, then draw message
		self.screen.fill(self.button_color, self.rect)#Draw the rectangle
		self.screen.blit(self.msg_image, self.msg_image_rect)#Draw the text IMAGE
