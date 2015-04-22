import sys
import os.path
import numpy as np
import cPickle as pickle

def next_time(rate):
	return -np.log(1. - np.random.random())/rate

def generate_arrivals(symbol_name,symbol_dist,symbol_rate,t_max):
	t = 0
	arrival_times = []

	while t < t_max:
		dt = next_time(symbol_rate)
		t += dt
		update = [t,symbol_name,np.random.normal(loc=symbol_dist[0],scale=symbol_dist[1])]
		arrival_times.append(update)
	### end while t < t_ma
	return np.array(arrival_times)


def main():
	if len(sys.argv) < 3:
		print 'Error, incorrect input.'
		print 'Usage: python ' + sys.argv[0] + ' symbol_params.pkl seeds.txt'
		exit()
	### end if len(sys.argv) < 3

	dist_param_filename = os.path.abspath(os.path.expanduser(sys.argv[1]))
	(t_max,symbol_dist,symbol_rate) = pickle.load(open(dist_param_filename,'rb'))
	seed_filename = os.path.abspath(os.path.expanduser(sys.argv[2]))
	seeds = list(np.loadtxt(seed_filename,dtype=np.uint32))

	for (idx,seed) in enumerate(seeds):
		print seed
		np.random.seed(seed)
		arrivals = None
		for symbol in symbol_dist.keys():
			symb_arr = generate_arrivals(symbol,symbol_dist[symbol],symbol_rate[symbol],t_max)
			if arrivals == None:
				arrivals = symb_arr
			else:
				arrivals = np.vstack((arrivals,symb_arr))
			### end if arrivals == None
		### end for symbol in symbols
		# sort and save the arrival rates
		arrivals = arrivals[arrivals[:,0].argsort()]
		arrivals[1:,0] = np.diff(arrivals[:,0])
		np.savetxt('../data/input/trial-'+str(idx).zfill(2)+'.txt',arrivals)
	### end for (idx,seed) in enumerate(seed)
### end main


if __name__=='__main__':
	main()
