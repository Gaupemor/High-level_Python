#!/bin/bash

error_message="This command only accepts one integer argument."

function climb() {
	i=1

	#on argument passed
	if [ $# -gt 0 ]; then
		#error case - if not integer arg OR more than one arg
		if ! [[ $1 =~ ^[0-9]+$ ]] || (($# > 2 )); then
			echo $error_message
			return
		else
			i=$1
		fi
	fi

	for num in $(seq 1 $i); do
		cd ../
	done
}
