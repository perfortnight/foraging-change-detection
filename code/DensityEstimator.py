import numpy as np
from scipy.optimize import fmin as minimize

def entropy(dist):
	support = dist.support()
# 	num_data_pts = max([100.,float(len(dist.data))])
# 	resolution = (support[1] - support[0])/num_data_pts
	resolution = 0.01
# 	print num_data_pts,support,resolution
	prob = [dist(x) for x in np.arange(support[0],support[1]+resolution,resolution)]	
	return -np.nansum([p*np.log(p)*resolution for p in prob])
### end entropy

def max_entropy(dist,h):
	dist.set_bw(h)
	return entropy(dist)
### end max_entropy

def all_but(arr,i):
	return np.concatenate((arr[:i],arr[i+1:]))

def cross_validation(f,h):
	f.set_bw(h)
	# integrate f
	supp = f.support()
	num_data_pts = 100. #max([100.,float(len(f.data))])
	res = (supp[1] - supp[0])/num_data_pts
	f_vals = [f(x) for x in np.arange(supp[0],supp[1],res)]
	intg = np.sum([fx*fx*res for fx in f_vals])
	# avoiding dots to speed up a little.
	n = float(len(f.data))
	data = f.data
	kernel = f.kernel
	bw = f.h
	cv_term = 0
	for i in np.arange(len(data)):
		for j in np.arange(i+1,len(data)):
			xi = data[i]
			xj = data[j]
			cv_term += kernel((xi-xj)/bw)
	### end for (i,x) in enumerate....
	
# 	for (i,xi) in enumerate(data):
# 		cv_term += sum([kernel((xi-xj)/bw) for xj in data[i+1:]])

	return intg - (4./(n*n*bw))*cv_term
### end cross_validation

def epanechnikov(u):
	if np.fabs(u) > 1:
		return 0.
	else:
		return 0.75*(1.-u*u)
### end 

def prob(x,data,kernel,bw):
	n = float(len(data))
	prob = np.sum([kernel((x-Xi)/bw) for Xi in data])/(bw*n)
	return prob
### end prob

class density_estimator:
	def __init__(self,h=1):
		self.kernel = epanechnikov 
		self.data = []
		self.h = h 
	### end __init__

	def set_bw(self,bw):
		# don't allow negative or zero bandwidths
		if bw > 0.:
			self.h = bw
		### end if
	### end set_bw

	def add_data(self,x):
		self.data.append(float(x))
	### end add_data

	def update(self,x):
		self.data.append(float(x))
		# optimise h for maximum entropy.
		if len(self.data) > 1:
			x0 = np.array([self.h])
			res = minimize(lambda x: cross_validation(self,x),x0,full_output=0,disp=0)
			self.h = res[0]
		### end if len(data > 1)
# 		print self.h,float(len(self.data))
	
	### end update

	def support(self):
		return (min(self.data)-self.h,max(self.data)+self.h)
	### end support

	def __call__(self,x):
		if len(self.data) == 0:
			return 0.0001
		### end if
		return prob(x,self.data,self.kernel,self.h)
	### end def __call__
### end class density_estimator


