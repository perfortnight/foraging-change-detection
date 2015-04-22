# The purpose of this script is to produce a graph that shows
# the reward as a function of the number of samples taken from
# a distribution.  

from scipy.stats import gaussian_kde
import matplotlib.pyplot as plt

import sys
sys.path.append('/opt/useful/python')
import plotting

import numpy as np


def reward(data,x):
	before = gaussian_kde(data)
	p1 = before(x)
	after = gaussian_kde(data.append(x))
	p2 = after(x)
	return -np.log(p2/p1)
### end reward


def main():
	np.random.seed(12148761)
### end main

if __name__=='__main__':
	main()
