import numpy as np
from numpy import ma
import matplotlib.pyplot as plt
from DensityEstimator import *

from scipy.stats import norm, uniform

import cPickle as pickle


def main():
	dist = density_estimator()
	seed = 201570123
	np.random.seed(seed)
	ent = []
	num_samples = 100
	samples = np.random.normal(loc=0.,scale=10.,size=(num_samples,1))
# 	samples = np.random.uniform(low=0.,high=1.,size=(num_samples,1))

	count = 0
	before = []
	after = []
	for sample in samples:
		before.append(dist(sample))
		dist.add_data(sample)
		dist.update()
		after.append(dist(sample))
# 		ent.append(entropy(dist))
		if count % 10 == 0:
			print 'sample ',count
		### end if count % 10 == 0
		count += 1
	### end for i in range(1000)

	
	pickle.dump((samples,before,after,dist),open('test-entropy.pkl','wb'))
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
