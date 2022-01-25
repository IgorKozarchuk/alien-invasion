from box import BoxElement

class Button(BoxElement):
	def __init__(self, ai_game, text):
		super().__init__(ai_game, text)
		self.background_paddings = {"x": 100, "y": 50}
		self.font_size = 40
		self.border_width = 5
		self._prep_box_element()
