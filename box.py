import pygame

class BoxElement():
	def __init__(self, ai_game, text):
		self.screen = ai_game.screen
		self.screen_rect = self.screen.get_rect()
		self.text = text
		self.text_color = (250, 50, 20)
		self.background_color = (0, 0, 0)
		self.background_paddings = {"x": 10, "y": 10}
		self.font_face = "Consolas"
		self.font_size = 18
		self.border_width = 2

		self._prep_box_element()

	def _prep_box_element(self):
		self.font = pygame.font.SysFont(self.font_face, self.font_size)
		self.text_image = self.font.render(self.text, True, self.text_color, self.background_color)
		self.text_image_rect = self.text_image.get_rect()
		self.text_image_rect.center = self.screen_rect.center
		self.rect = self.text_image_rect.inflate(self.background_paddings["x"], self.background_paddings["y"])

	def draw_box_element(self):
		self.screen.fill(self.background_color, self.rect)
		self.screen.blit(self.text_image, self.text_image_rect)
		#border
		pygame.draw.rect(self.screen, self.text_color, self.rect, self.border_width)
