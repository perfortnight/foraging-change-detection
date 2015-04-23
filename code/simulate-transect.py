import numpy as np
import os.path
import sys
from sampling import *
import cPickle as pickle

from scipy.integrate import quad
from scipy.stats import gaussian_kde,norm

import warnings

#warnings.filterwarnings('error')


def score_integrand(x,p,q):
	return np.abs(p.pdf(x)-q(x))

def kl_integrand(x,p,q):
# 	print p(x),q(x)
	a = p.pdf(x)*np.log(p.pdf(x))
	b = p.pdf(x)*np.log(q(x))

	return a - b
### end kl_integrand

def entropy_integrand(x,p):
	return -p.pdf(x)*np.log(p.pdf(x))

def make_estimator(data):
	if len(data) == 0:
		return lambda x: 0.000001
	elif len(data) == 1:
		dist = norm(loc=data[0],scale=1.)
		return lambda x: dist.pdf(x)
	else:
		return gaussian_kde(data)

def score(agent,truth):
	symbols = truth.keys()
	score = 0.
	results = []
	for symbol in symbols:
		integral = None
		tail_len = 4*truth[symbol].var()
		true_mean = truth[symbol].mean()
		int_range = [true_mean - tail_len,true_mean + tail_len]
		estimator = None
		if symbol in agent.samples.keys():
			samples = agent.samples[symbol]
			estimator = make_estimator(samples)
		else:
			estimator = make_estimator([])
		# fit kde
# 		print symbol, samples
		# use the scipy integrator to compute the kl divergence.
		integral = quad(score_integrand,int_range[0],int_range[1],args=(truth[symbol],estimator),limit=100)
		#else:
		#	# Compute the entropy of the true distribution and take all those 
		#	# points 
		#	integral = quad(entropy_integrand,int_range[0],int_range[1],args=(truth[symbol],))
		### end if
		score += integral[0]
		num_samples = 0
		if symbol in agent.samples.keys():
			num_samples = len(agent.samples[symbol])
		### end if
		results.append((symbol,num_samples,integral[0]))
	### end for
	return (results,score)
### end score

def main(trial_name,param_data_file,agent_type,sample_cost):
	#sample_cost = 1e-1 # arbitrary number. 
										 # If you scale the time range do the same here.
	max_time = 1000.
	# load transect
	trial = np.loadtxt(trial_name)
	param_data = pickle.load(open(param_data_file,'rb'))
	params = param_data[1]
	truth = {k: norm(loc=params[k][0],scale=params[k][1]) for k in params.keys()}
	# instantiate the agent
	# run agent on transect
	agent = None
	if agent_type == 'uniform':
		agent = UniformSampling()
	elif agent_type == 'foraging':
		agent = ForagingSampling()
	### end if

	for option in trial:
		#print option	
		time = option[0]
		symbol = int(option[1])
		value = option[2]
		cost = sample_cost
		action = agent(time,symbol)
		if action == 'sample':
			agent.update(time,symbol,value,cost)
			# In the future with random costs:
			#agent.update(option[1],option[2],option[3])
		# end if
	# compute error from true distributions.
		if agent.current_time > max_time:
			break
		# end if
	# end for
	print score(agent,truth)

### end main

if __name__=='__main__':
	trial_name = os.path.abspath(os.path.expanduser(sys.argv[1]))
	params_data = os.path.abspath(os.path.expanduser(sys.argv[2]))
	agent_type = sys.argv[3]
	sample_cost = float(sys.argv[4])
	main(trial_name,params_data,agent_type,sample_cost)
