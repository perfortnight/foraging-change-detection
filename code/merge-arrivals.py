import sys
import os.path
import numpy as np

def main():
	if len(sys.argv) < 3:
		print 'Requires 2 or more files to merge'
		print 'Proper usage: '
		print 'python -u file1.txt file2.txt ... fileN.txt'
	### end if len(sys.argv) < 3
	result = None
	for i in range(1,len(sys.argv)):
		full_name = os.path.abspath(os.path.expanduser(sys.argv[i]))
		data = np.loadtxt(full_name)
		if result == None:
			result = data
		else:
			result = np.vstack((result,data))
		### end if result == None
	### end for i in range(1,len(sys.argv))
	sorted_result = result[result[:,0].argsort(axis=0)]
	np.savetxt('merged-arrivals.txt',sorted_result)


if __name__=='__main__':
	main()
