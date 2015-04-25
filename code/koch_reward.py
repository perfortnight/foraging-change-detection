import numpy as np
from scipy.stats import norm, uniform, gaussian_kde

def prob(data,x):
	retval = 0.000000000001
	if len(data) == 0:
		retval = 0.000001
	### end if
	elif len(data) == 1:
		n = norm(loc=data[0],scale=1.)
		retval += n.pdf(x)
# 		min_val = min(data[0],0.)
# 		max_val = max(data[0],0.)
# 		print min_val,max_val
# 		u = uniform(loc=min_val,scale=max_val)
# 		retval = u.pdf(x)
	else:
		pdf = gaussian_kde(data)
		retval += pdf(x)
	### end if

	return retval
### end prob

def reward(data,x):
	p_before = prob(data,x)
	try:
		assert (p_before > 0)
	except AssertionError:
		print data, x, p_before
		assert(False)

	### end try/except
	data.append(x)
	p_after = prob(data,x)
	if len(data) > 1:
		return np.log(p_after/p_before)
	else:
		return -np.log(p_after)
### end reward


