#!/bin/bash

agent_type=$1
params=$2
# if we supply an argument for it, set the sample cost.
sample_cost=0.1
if (( $# > 2 )); then
	sample_cost=$3
fi


for i in $(ls ../data/input/$params/trial-*txt); do 
	mkdir -p ../data/output/$params;
	python -u simulate-transect.py $i ../data/input/$params-params.pkl $agent_type $sample_cost | tee -a ../data/output/$params/${agent_type}-cost-${sample_cost}-results.txt;
done

