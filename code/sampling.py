import numpy as np
from collections import Counter
from scipy.stats import gaussian_kde

import koch_reward

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
		self.current_time = 0.
		self.symbol_iat = {}  # interarrival times.
		self.last_time_seen = {}  # interarrival times.
		self.cost = {}
		self.rewards = {}
		self.samples = {}
	### end __init__

	def dist_value(self,symbol):
		# Consider predicting the next reward from the previous one.
		# Should be able to learn a curve here.
		return np.mean(self.rewards[symbol])/(np.mean(self.symbol_iat[symbol]) + np.mean(self.cost[symbol]))
	### end value

	def value(self,symbol):
		return np.mean(self.rewards[symbol])/np.mean(self.cost[symbol])

	def env_value(self):
		# should this be:
		# rate_{symb} = avg_{symb}[value]/(avg_{symb}[iat]+sampling_time)
		# We want this one ultimately:
		# avg_{symb}[value]/(avg_{symb}[iat]+avg_{symb}[sampling_time])
		# should we then do an empirical average or a sum?
		# The other alternative would be avg_{symb}[value]/(avg[iat] + avg_{symb}[sampling_time])
		# where we learn the probability of which symbol we'd encounter at any given time.
		num_keys = len(self.samples.keys())
		result = np.mean([self.dist_value(key) for key in self.samples.keys()])
		return result
	### end env_value

	def __call__(self,time,symb):
		retval = None
		self.current_time += time
		self.last_time_seen[symb] = self.current_time
		symbol_dt = self.last_time_seen[symb]
		if symb not in self.samples.keys():
			self.samples[symb] = []
			self.rewards[symb] = []
			self.symbol_iat[symb] = []

			retval = 'sample'
		else:
			sampling_cost = np.mean(self.cost[symb])
			symbol_value = self.value(symb)
			env_value = self.env_value()
# 			print symbol_value,sampling_cost, env_value
			if symbol_value/sampling_cost >= env_value:
				retval = 'sample'
			### end

			# What you'd need to do for all the symbols.
			# update interarrival time
			old_time = self.last_time_seen[symb]
			# convert to zero for first time
			symbol_dt = self.last_time_seen[symb] - old_time
			### end if
		### end
		self.symbol_iat[symb].append(symbol_dt)

		return retval
	### end query

	def update(self,time,symb,val,cost):
		# Compute reward
		self.current_time += cost
		# In the default case we have to show some improvement.
		# Make it the same for all of them so they have the same
		# starting point, why not?
# 		before = lambda x: 0.0000001
# 		after = lambda x: 0.00001
# 		if len(self.samples[symb]) > 1:
# 			try:
# 				before = gaussian_kde(self.samples[symb])
# # 			except (RuntimeError,TypeError,NameError,ValueError):
# 			except np.linalg.linalg.LinAlgError:
# 				print 'Before singular matrix:'
# 				print self.samples
# 		### end if
# 		self.samples[symb].append(val)
# 		if len(self.samples[symb]) > 1:
# 			try:
# 				after = gaussian_kde(self.samples[symb])
# # 			except (RuntimeError,TypeError,NameError,ValueError):
# 			except np.linalg.linalg.LinAlgError:
# 				print 'After singular matrix:'
# 				print self.samples
# 		### end if
# 
# 		reward = np.log(after(val)/before(val))

		len_before = len(self.samples[symb])
		reward = koch_reward.reward(self.samples[symb],val)
		len_after = len(self.samples[symb])
		assert(len_before != len_after)

# 		print symb, reward
		### end if
		self.rewards[symb].append(reward)

		# Update the cost of sampling
		self.cost[symb] = cost
# 		self.samples[symb].append(val)
		# update time since last seen.
		### end if

	### end update

### end class ForagingSampling

class UniformSampling:
	def __init__(self):
		self.symbols = []
		self.distribution = Counter()
		self.samples_taken = 0
		self.samples= {}
		self.current_time = 0.
	### end __init__

	def __call__(self,time,symb):
		retval = None
		self.current_time += time
	
		if len(self.distribution.values()) == 0:
			retval = 'sample'
		elif (self.distribution[symb] < max(self.distribution.values()) or \
				  self.distribution[symb] == min(self.distribution.values()) ):
			retval = 'sample'
			self.samples_taken += 1
		### end 
		return retval
	### end query

	def update(self,time,symb,val,cost):
		self.current_time += cost
		self.distribution.update([symb])
		if not symb in self.samples.keys():
			self.samples[symb] = []
		### end
		#print symb, self.samples[symb]
		self.samples[symb].append(val)
	### end update

### end class UniformSampling

class ExhaustiveSampling:
	def __init__(self):
		self.symbols = []
		self.distribution = Counter()
		self.samples_taken = 0
		self.samples= {}
		self.current_time = 0.
	### end __init__

	def __call__(self,time,symb):
		retval = 'sample' 
		self.current_time += time
	
# 		if len(self.distribution.values()) == 0:
# 			retval = 'sample'
# 		elif (self.distribution[symb] < max(self.distribution.values()) or \
# 				  self.distribution[symb] == min(self.distribution.values()) ):
# 			retval = 'sample'
# 			self.samples_taken += 1
# 		### end 
		return retval
	### end query

	def update(self,time,symb,val,cost):
		self.current_time += cost
		self.distribution.update([symb])
		if not symb in self.samples.keys():
			self.samples[symb] = []
		### end
		#print symb, self.samples[symb]
		self.samples[symb].append(val)
	### end update
