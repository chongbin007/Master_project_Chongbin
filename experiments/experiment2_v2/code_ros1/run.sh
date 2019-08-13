#!/bin/bash

RESULTS_FOLDER="results"

CURRENT_FREQ=100
N_RUNS=3

mkdir $RESULTS_FOLDER -p

for((CURRENT_RUN=1;$CURRENT_RUN<=$N_RUNS;++CURRENT_RUN)) do
	RUN_FOLDER="$RESULTS_FOLDER/run_$CURRENT_RUN/"
	mkdir $RUN_FOLDER -p
	echo "Running Frequency: $CURRENT_FREQ KHz"
	rosrun rosberry_experiments test_latency_main.py $CURRENT_FREQ
	mv "times_$CURRENT_FREQ.csv" $RUN_FOLDER	
done