#!/bin/bash

# Description: 
# This script was created to automate the process of running the PydTfinder script.
# You can modify the below code in terms of your needs.

# LOOP 1: Delta T modifications
for DT in 1 2 3 5 10 20 30 50 # Manipulate the delta T values here
do
	echo 0 | python3 PydTfinder.py -it csv -dt $DT -l delT_modifications_${DT}K
done

# LOOP 2: the number of points modifications
for NP in {5..10} # Manipulate the number of points here 
do
	echo 0 | python3 PydTfinder.py -it csv -n $NP -l NP_modifications_${NP}points
done

echo "INFO All automations have been completed!"
sleep 1

# QUIT
exit 0
