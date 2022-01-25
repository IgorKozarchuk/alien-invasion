import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
	def __init__(self, ai_game):
		super().__init__()
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.screen_rect = ai_game.screen.get_rect()

		#self.image = pygame.image.load("images/ship.png") #comment for development, uncomment for converting to .exe
		self.image = pygame.image.load("PROJ1_Alien_Invasion_Game/images/ship.png") #uncomment for development, comment for converting to .exe
		self.rect = self.image.get_rect()
		self.rect.midbottom = self.screen_rect.midbottom

		self.x = float(self.rect.x)

		self.moving_right = False
		self.moving_left = False
	
	def update(self):
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.x += self.settings.ship_speed
		if self.moving_left and self.rect.left > 0:
			self.x -= self.settings.ship_speed
		self.rect.x = self.x

	def blitme(self):
		self.screen.blit(self.image, self.rect)

	def center_ship(self):
		self.rect.midbottom = self.screen_rect.midbottom
		self.x = float(self.rect.x)

class ShipSmall(Ship):
	def __init__(self, ai_game):
		super().__init__(ai_game)
		#self.image = pygame.image.load("images/ship_small.png") #comment for development, uncomment for converting to .exe
		self.image = pygame.image.load("PROJ1_Alien_Invasion_Game/images/ship_small.png") #uncomment for development, comment for converting to .exe
		self.rect = self.image.get_rect()
