import pyglet
from app import window_width, window_height

class PhysicalObject(pyglet.sprite.Sprite):

	def __init__(self, *args, **kwargs):
		super(PhysicalObject, self).__init__(*args, **kwargs)

		self.velocity_x, self.velocity_y = 0.0, 0.0
	
	def check_bounds(self):
		min_x = -self.image.width/2
		min_y = -self.image.height/2
		max_x = app.window_width + self.image.width/2
		max_y = app.window_height + self.image.width/2

		if self.x < min_x:
			self.x = max_x
		elif self.x > max_x:
			self.x = min_x
		if self.y < min_y:
			self.y = max_y
		elif self.y > max_y:
			self.y = min_y

	def update(self, dt):
		self.x += self.velocity_x * dt
		self.y += self.velocity_y * dt
		self.check_bounds()

