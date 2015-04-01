# Mateusz Gawron, grupa sroda 8:00
# Sposob uruchamiania:
# np. python script2.py

import random
import time

class Generator:
	def get_data(self):
		is_left = random.random() < 0.5
		angle = random.random() * 10.0
		time = random.random() * 0.5 + 0.5
		return (is_left, angle, time)
		
class Pilot:
	def __init__(self, generator):
		self.generator = generator
		self.minute = 0
		self.second = 0
	def make_correction(self):
		self.data = self.generator.get_data()
		self.speed = self.data[1]/self.data[2]
		self.before_side = ""
		self.after_side = ""
		if self.data[0]:
			self.before_side = "lewo"
			self.after_side = "prawo"
		else:
			self.before_side = "prawo"
			self.after_side = "lewo"
		minute_str = str(self.minute).zfill(2)
		second_str = str(self.second).zfill(2)
		print "["+minute_str+":"+second_str+"]",
		print "Wykryto przechylenie w "+self.before_side
		print str(round(self.data[1],2)) + " stopni",
		print "w czasie "+str(round(self.data[2],2))+" s",
		print "(v = "+str(round(self.speed,2))+" st./s)"
		print "Korekcja w "+self.after_side+" o",
		print str(round(self.speed,2))+" stopni"
		print ""
		
	def make_timestep(self):
		self.second = self.second+1
		if (self.second == 60):
			self.second = 0
			self.minute = self.minute+1
			if (self.minute == 60):
				self.minute = 0
	
def run():
	gen = Generator()
	pilot = Pilot(gen)
	while True:
		pilot.make_correction()
		time.sleep(1)
		pilot.make_timestep()
	
run()
	