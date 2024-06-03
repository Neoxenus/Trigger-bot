import numpy as np
import time
from time import sleep

class DelayManager:
	def __init__(self, base_delay, random_delay):
		self.base_delay = base_delay
		self.random_delay = random_delay
		self.rng = np.random.default_rng()
	
	def make_shoot_delay(self):
		delay_percentage = self.random_delay / 100.0 * self.rng.random()
		actual_delay = self.base_delay + self.base_delay * delay_percentage
		time.sleep(actual_delay)

	def make_check_delay(self):
		time.sleep(0.1)
