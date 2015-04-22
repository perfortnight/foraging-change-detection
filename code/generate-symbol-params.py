import cPickle as pickle
import os.path
import numpy as np


def main():
	max_symbols = 6
	symbols = range(max_symbols)
	
	t_max = 1000.

	# arbitrary random variables
# 	dist_name='arbitrary'
# 	rate_name='diff'
# 	symbol = {0: (0.,1.),\
# 			1: (10.,0.1),\
# 			2: (0.,5.),\
# 			3: (2.,4.),\
# 			4: (-2,4.),\
# 			5: (0.,0.1)}
# 	symbol_rates = {0:1.,1:0.8,2:0.9,3:1.1,4:1./20.,5:1.1}

	# Identically distributied random variables
# 	dist_name = 'ident'
# 	rate_name = 'diff'
# 	symbol = {0: (0.,1.),\
# 			1: (0.,1.),\
# 			2: (0.,1.),\
# 			3: (0.,1.),\
# 			4: (0.,1.),\
# 			5: (0.,1.)}
# 	symbol_rates = {0:1.,1:0.8,2:0.01,3:10.,4:1./20.,5:100.}

	# Identical distributions with identical arrival rates
# 	dist_name = 'ident'
# 	rate_name = 'ident'
# 	symbol = {0: (0.,1.),\
# 			1: (0.,1.),\
# 			2: (0.,1.),\
# 			3: (0.,1.),\
# 			4: (0.,1.),\
# 			5: (0.,1.)}
# 	symbol_rates = {0:1.,1:1.,2:1.,3:1.,4:1.,5:1.}

	# One fat distribution, identical arrival rates
# 	dist_name = 'fat1'
# 	rate_name = 'ident'
# 	symbol = {0: (0.,1.),\
# 			1: (0.,1.),\
# 			2: (0.,1.),\
# 			3: (0.,1.),\
# 			4: (0.,1.),\
# 			5: (0.,100.)}
# 	symbol_rates = {0:1.,1:1.,2:1.,3:1.,4:1.,5:1.}

	# One fat distribution, identical arrival rates
	dist_name = 'skinny1'
	rate_name = 'ident'
	symbol = {0: (0.,1.),\
			1: (0.,1.),\
			2: (0.,1.),\
			3: (0.,1.),\
			4: (0.,1.),\
			5: (0.,0.1)}
	symbol_rates = {0:1.,1:1.,2:1.,3:1.,4:1.,5:1.}




	outfile = open('../data/input/'+dist_name+'-'+rate_name+'-params.pkl','wb')
	pickle.dump((t_max,symbol,symbol_rates),outfile)
	outfile.close()
### end main


if __name__=='__main__':
	main()
