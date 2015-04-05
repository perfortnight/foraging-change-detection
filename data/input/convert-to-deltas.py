import numpy as np
import os.path
import sys

def main(infile,outfile):
	a = np.loadtxt(infile)
	results = np.zeros(a.shape)
	results[:,1:] = a[:,1:]
	results[0,0] = a[0,0]
	results[1:,0] = np.diff(a[:,0])

	np.savetxt(outfile,results)
	

if __name__=='__main__':
	infile = os.path.abspath(os.path.expanduser(sys.argv[1]))
	outfile = os.path.abspath(os.path.expanduser(sys.argv[2]))
	print infile, outfile
	main(infile,outfile)
