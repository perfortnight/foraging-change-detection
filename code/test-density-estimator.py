import numpy as np
import os.path
import cPickle

from DensityEstimator import * 


def main():
	out_name = 'surprise.pkl'
	if os.path.isfile(out_name):
		print 'back up pickle file first'
		exit()
	### end if os.path.isfile(out_name)
	outfile = open(out_name,'wb')
	seeds = np.loadtxt('seeds.txt')
	print seeds

	# wolog we can use loc = 0 for all normal distributions.
# 	scales = [0.001,0.2,1.,5.,10.]
	scales = [0.01,1.,10.]

	scale_results = []
	for scale in scales:
		seed_results = None
		for seed in seeds[:10]:
			np.random.seed(int(seed))
			dist = density_estimator()# make the Kernel density estimator
			# do the simulation.
			num_samples = 100
# 			samples = np.random.normal(loc=0.,scale=scale,size=(num_samples,1))
			samples = np.random.uniform(low=0.,high=scale,size=(num_samples,1))
			count = 0
			before = np.zeros((num_samples,1))
			after = np.zeros((num_samples,1))
			for sample in samples:
				# take a sample,
# 				sample = np.random.normal(loc=1.,scale=scale)
				before[count] = dist(sample)
# 				dist.add_data(sample)
				dist.update(sample)
				after[count] = dist(sample)
				# compute the self information.
# 				self_info1 = self_info2
				count += 1
			### end for count in range
			reward = np.log(after/before)
			if seed_results == None:
				seed_results = reward #np.array([reward])
			else:
				seed_results = np.vstack((seed_results,reward))
			### end if seed_results == None
		### end for seed in seeds
		scale_results.append(seed_results)
		print 'Finished scale ' + str(scale)
	### end for scale in scales
	# save the data.
	cPickle.dump(scale_results,outfile)
### end main


if __name__=='__main__':
	main()
