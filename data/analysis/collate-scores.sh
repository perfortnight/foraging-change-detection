#!/bin/bash

case=$1
dest_dir=../output/${case}
dest_file=${dest_dir}/${case}-scores.dat

for cost in 0.001 0.01 0.1 1.0 2.0 5.0 8.0 10.0 20.0 50.0 80.0 100.0 120.0 150.0 ; do

	echo "# ${cost} " >> $dest_file
	python -u compute-mean.py  ${dest_dir}/cost-${cost}.txt >> $dest_file
	echo "" >> $dest_file
	echo "" >> $dest_file
done
