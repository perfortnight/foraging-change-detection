import numpy as np
import matplotlib as mpl 
import matplotlib.pyplot as plt
import os.path
import sys
sys.path.append('/opt/useful/python/')
import plotting

def main():
	plotting.init()
	filename = os.path.abspath(os.path.expanduser(sys.argv[1]))
	a = np.loadtxt(filename)
	(base,ext) = os.path.splitext(filename)
	print base

	vals = a[:,0]
	uni_mu = a[:,1]
	uni_std = a[:,2]
	f_mu = a[:,3]
	f_std = a[:,4]

	plt.hold(True)
	plotting.plot_confidence(uni_mu,uni_std,'-','b',vals=vals,confidence=1.96)
	plotting.plot_confidence(f_mu,f_std,'-','orange',vals=vals,confidence=1.96)
	axis = plt.gca()
	axis.set_xscale('log')
	axis.set_xscale('log')
#  	plotting.adjust_spines(axis)
	plt.xlabel('Sampling cost (arbitrary time)')
	plt.ylabel('Total error in distributions (arbitrary units)')
	plt.title('Accumulated error vs. sampling cost (N=21)')
	plt.legend(('Uniform','Foraging'),loc=2)

	outname = base + '.pgf'
	print outname
	plt.show()
	#plt.savefig(outname,dpi=500)

if __name__=='__main__':
	main()
