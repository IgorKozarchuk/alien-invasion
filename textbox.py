from box import BoxElement

class TextBox(BoxElement):
	def __init__(self, ai_game, text):
		super().__init__(ai_game, text)
		self.background_paddings = {"x": 30, "y": 30}
		self.font_size = 24
		self.border_width = 3
		self._prep_box_element()
