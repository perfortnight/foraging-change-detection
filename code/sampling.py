import numpy as np
from collections import Counter

# Considering two different foraging algorithms.
# The first is one that considers the arrival times of each
# different sampling type and computes the environment value that way
# The second just looks at the inter-event arrival rate, regardless of type
# and computes the expected value based on arrival statistics, then 
# computes the environment value that way.

class ForagingSampling:
	def __init__(self):
		self.symb_arrival_time = {}
		self.last_symbol_time = {}
		self.symbol_frequency  = Counter()
	### end __init__

	def query(self,time,symb):
		pass
	### end query

	def update(self,time,symb,val):
		pass
	### update
### end class ForagingSampling
