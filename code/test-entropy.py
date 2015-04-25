import numpy as np
from numpy import ma
import matplotlib.pyplot as plt
from DensityEstimator import *

from scipy.stats import norm, uniform, gaussian_kde

import sys
sys.path.append('/opt/useful/python')
import plotting

import koch_reward


def get_cumulative_values(num_samples):

# 	samples = np.random.normal(loc=0.,scale=1.,size=(num_samples,1))
	samples = np.random.uniform(low=0.,high=1.,size=(num_samples,1))

	count = 0
	data = []
	values = []
	for sample in samples:
		values.append(koch_reward.reward(data,sample[0]))
# 		if count % 10 == 0:
# 			print 'sample ',count
		### end if count % 10 == 0
		count += 1
	### end for i in range(1000)
	return np.cumsum(values)

### end get_cumulative_values


def main():
	plotting.init()
	dist = density_estimator()
	seeds = [201570123,17526317,81715,1270957,6571]
	ent = []
	num_samples = 4000
	value = np.zeros((len(seeds),num_samples))
	for (idx,seed) in enumerate(seeds):
		np.random.seed(seed)
		value[idx,:] = get_cumulative_values(num_samples)
	### end for

	plt.figure(1)
	v_mu = np.mean(value,axis=0)
	diff_v = np.zeros(v_mu.shape)
	diff_v[0] = v_mu[0]
	diff_v[1:] = np.diff(v_mu)
	plt.plot(range(num_samples),diff_v)

	plt.figure(2)
	plotting.plot_confidence(np.mean(value,axis=0),np.std(value,axis=0)/np.sqrt(len(seeds)),'-','b')
	ax = plt.gca()
	plotting.adjust_spines(ax)

	plt.title('Average cumulative value vs number of samples taken.  N = %d' % (len(seeds)))
	plt.xlabel('Number of samples')
	plt.ylabel('Cumulative Reward')

	plt.show()

	
# 	pickle.dump((samples,before,after,dist),open('test-entropy.pkl','wb'))
# 
# 	plt.figure(1)
# 
# 	sample_count = range(num_samples)
# # 	plt.plot(sample_count,ent,'r-')
# 	plt.hold(True)
# 	plt.plot(sample_count,before,'r-')
# 	plt.plot(sample_count,after,'b-')
# 
# 	plt.figure(3)
# # 	plt.plot(sample_count[:-1],np.fabs(np.diff(ent)),'g-')
# 	raw_reward = np.log(np.array(after)/np.array(before))
# 	reward = ma.masked_array(raw_reward, mask = np.isnan(raw_reward),fill_value = 0.)
# 	value = np.cumsum(reward)/sample_count+1
# 	plt.hold(True)
# 	plt.plot(sample_count,reward,'g-')
# 	plt.plot(sample_count,value,'r-')
# 	plt.hold(False)
# 
# 
# 	plt.figure(2)
# 	x_data = np.arange(-20,20,0.01)
# 	rv = norm(loc=0.,scale=10.)
# 	x_data = np.arange(-20,20.,0.01)
# # 	rv = uniform(loc=0.,scale=1.)
# 	p_x = [rv.pdf(x) for x in x_data]
# 	f_x = [dist(x) for x in x_data]
# 
# 	plt.hold(True)
# 	plt.plot(x_data,p_x,'r-')
# 	plt.plot(x_data,f_x,'b-')
# 	plt.plot(samples,np.zeros((len(samples),1)),'x')
# 	plt.hold(False)
# 	plt.show()
# 	

if __name__=='__main__':
	main()
