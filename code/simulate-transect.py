import numpy as np
import os.path
import sys


def main(trial_name):
	trial = np.loadtxt(trial_name)
	# load transect
	# instantiate the agent
	# run agent on transect
	for option in trial:
		print option	
	# compute error from true distributions.

	

### end main

if __name__=='__main__':
	trial_name = os.path.abspath(os.path.expanduser(sys.argv[1]))
	main(trial_name)
