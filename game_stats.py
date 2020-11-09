class GameStats():
	def __init__(self, ai_settings):
		self.ai_settings = ai_settings
		self.game_active = False
		self.hi_path = 'high_score.txt'
		with open(self.hi_path) as file_object:
			self.high_score = file_object.read()
			if self.high_score:
				self.high_score = int(self.high_score)
		self.reset_stats()

	def reset_stats(self):#initialize stats that can change during the game
		self.ships_left = self.ai_settings.ship_limit
		self.score = 0 #0
		self.level = 1


 
