import numpy as np
import os.path
import sys

def main():
	filename = os.path.abspath(os.path.expanduser(sys.argv[1]))
	data = np.loadtxt(filename)
	(num_trials,num_vars) = data.shape
	mu = np.mean(data,axis=0)
	std = np.std(data,axis=0)/np.sqrt(num_trials)
	result = np.vstack((mu,std)).T
	print np.savetxt(sys.stdout,result,fmt='%.4f')

if __name__=='__main__':
	main()
