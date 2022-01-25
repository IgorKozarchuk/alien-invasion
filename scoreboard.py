import pygame.font
from pygame.sprite import Group
from ship import ShipSmall

class Scoreboard():
	def __init__(self, ai_game):
		self.ai_game = ai_game
		self.screen = ai_game.screen
		self.screen_rect = self.screen.get_rect()
		self.settings = ai_game.settings
		self.stats = ai_game.stats

		self.score_text_color = (98, 212, 22)
		self.high_score_text_color = (250, 250, 50)
		self.font = pygame.font.SysFont("Consolas", 24)

		self.prep_score()
		self.prep_high_score()
		self.prep_level()
		self.prep_ships()

	def prep_score(self):
		score_str = "Score: " + str(self.stats.score)
		self.score_image = self.font.render(score_str, True, self.score_text_color)

		self.score_rect = self.score_image.get_rect()
		self.score_rect.centerx = self.screen_rect.centerx
		self.score_rect.top = 10

	def prep_high_score(self):
		high_score_str = "High score: " + str(self.stats.high_score)
		self.high_score_image = self.font.render(high_score_str, True, self.high_score_text_color)

		self.high_score_rect = self.high_score_image.get_rect()
		self.high_score_rect.right = self.screen_rect.right - 20
		self.high_score_rect.top = self.score_rect.top
	
	def prep_level(self):
		level_str = "Level: " + str(self.stats.level)
		self.level_image = self.font.render(level_str, True, self.score_text_color)

		self.level_rect = self.level_image.get_rect()
		self.level_rect.centerx = self.screen_rect.centerx
		self.level_rect.top = self.score_rect.top + 25

	def prep_ships(self):
		self.ships = Group()
		for ship_number in range(self.stats.ships_left):
			ship = ShipSmall(self.ai_game)
			ship.rect.x = 20 + (ship.rect.width + 10) * ship_number
			ship.rect.y = self.score_rect.top
			self.ships.add(ship)

	def show_score(self):
		self.screen.blit(self.score_image, self.score_rect)
		self.screen.blit(self.high_score_image, self.high_score_rect)
		self.screen.blit(self.level_image, self.level_rect)
		self.ships.draw(self.screen)

	def check_high_score(self):
		if self.stats.score > self.stats.high_score:
			self.stats.high_score = self.stats.score
			self.prep_high_score()
