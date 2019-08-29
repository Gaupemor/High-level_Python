#!/bin/bash

function climb() {
	i=1

	if [ $# -gt 0 ]; then
		i=$1
	fi
	
	for num in $(seq 1 $i);
	do cd ../; done;
}
