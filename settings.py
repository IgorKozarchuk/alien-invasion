import pygame

class Settings:
	def __init__(self):
		self.screen_width = 1500
		self.screen_height = 1000
		self.bg_color = (10, 5, 40)
		#self.bg_img = pygame.image.load("images/space_bg.jpg") #comment for development, uncomment for converting to .exe
		self.bg_img = pygame.image.load("PROJ1_Alien_Invasion_Game/images/space_bg.jpg") #uncomment for development, comment for converting to .exe
		self.bg_img = pygame.transform.scale(self.bg_img, (self.screen_width, self.screen_height))
		self.ship_limit = 3

		self.bullet_width = 5
		self.bullet_height = 30
		self.bullet_color = (255, 100, 20)
		self.bullets_allowed = 3

		self.fleet_drop_speed = 20

		self.speedup_scale = 1.1
		self.fleet_direction = 1 #1 - right, -1 - left

		self.score_scale = 1

		self.initialize_dynamic_settings()

	def initialize_dynamic_settings(self):
		self.ship_speed = 3
		self.bullet_speed = 2.5
		self.alien_speed = 1.5
		self.alien_points = 1

	def increase_speed(self):
		self.ship_speed *= self.speedup_scale
		self.bullet_speed *= self.speedup_scale
		self.alien_speed *= self.speedup_scale
		self.alien_points = int(self.alien_points * self.score_scale)
