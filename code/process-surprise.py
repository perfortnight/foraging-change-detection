import sys
import os.path

sys.path.append('/opt/useful/python/')
import plotting

import cPickle as pickle
import numpy as np
from numpy import ma
import matplotlib.pyplot as plt

def value(rewards):
	msk_rwd = ma.masked_array(rewards,mask=(np.isnan(rewards)|np.isinf(rewards)),fill_value=0.)
	return np.cumsum(msk_rwd)/(np.arange(len(rewards))+1.)


def main():
	filename = os.path.abspath(os.path.expanduser(sys.argv[1]))
	data = pickle.load(open(filename,'rb'))
	print len(data)

	mean = []
	std_dev = []

# 	scales = ['0.001','0.2','1.','5.','10.']
	scales = ['0.01','1.','10.']
	plt.figure(1)
	plt.plot(True)
	counter = 0
	rewards = []
	std_err = []
	colour = ['r','b','g']
	fmt = ['-','-','-']
	for datum in data:
		values = None
		(rows,cols) = datum.shape
		dat = datum.reshape((10,100))
		reward = ma.masked_array(dat,mask=(np.isnan(dat)|np.isinf(dat)),fill_value=0)
		mean_reward = np.mean(np.cumsum(reward,axis=1),axis=0)
# 		rewards.append(ma.masked_array(mean_reward,mask=(np.isnan(mean_reward)|np.isinf(mean_reward)),fill_value=0.))
		std_reward = np.std(reward,axis=0)
		std_err.append(std_reward)


		for x in reward:
			val = value(x)
			if values == None:
				values = val
			else:
				values = np.vstack((values,val))
			### end if values == None
		### end for x in datum
		m = np.mean(np.cumsum(values,axis=1),axis=0)
		mean.append(m)
		s = np.std(np.cumsum(values,axis=1),axis=0)/np.sqrt(rows)
		std_dev.append(s)
		x_vals = np.arange(100)
# 		plt.errorbar(x_vals,m,yerr=s,label=scales[counter])
		plotting.plot_confidence(m[:30],s[:30],fmt[counter],colour[counter],vals=x_vals[:30],confidence=1.96)
		counter += 1
	### for datum in data
	plt.hold(False)
	plt.legend(('width=0.01','width=1','width=10'))

# 	plt.figure(2)
# 	plt.hold(True)
# 	for (i,r) in enumerate(rewards):
# 		plt.errorbar(np.arange(100),r,yerr=std_err[i])
# 	plt.hold(False)
# 	plt.legend((scales))


	plt.show()


if __name__=='__main__':
	main()
