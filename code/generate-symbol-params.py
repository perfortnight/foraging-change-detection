import cPickle as pickle
import os.path
import numpy as np


def main():
	max_symbols = 6
	symbols = range(max_symbols)
	
	t_max = 1000.

	symbol = {0: (0.,1.),\
			1: (10.,0.1),\
			2: (0.,5.),\
			3: (2.,4.),\
			4: (-2,4.),\
			5: (0.,0.1)}

	symbol_rates = {0:1.,1:0.8,2:0.9,3:1.1,4:1./20.,5:1.1}

	outfile = open('../data/input/dist-params.pkl','wb')
	pickle.dump((t_max,symbol,symbol_rates),outfile)
	outfile.close()
### end main


if __name__=='__main__':
	main()
