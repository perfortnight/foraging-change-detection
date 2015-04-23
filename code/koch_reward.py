import numpy as np
from scipy.stats import norm, uniform, gaussian_kde

def prob(data,x):
	if len(data) == 0:
		return 0.000001
	### end if
	if len(data) == 1:
		n = norm(loc=data[0],scale=1.)
		return n.pdf(x)
	### end if

	pdf = gaussian_kde(data)
	return pdf(x)
### end prob

def reward(data,x):
	p_before = prob(data,x)
	data.append(x)
	p_after = prob(data,x)
	return np.log(p_after/p_before)
### end reward


