#!/bin/bash

#Expects path to LOGFILE to exist.
#Creates LOGFILE if it does not exists in the LOGFILE path.
current_task=""
task_is_running=false
current_start_time=""
current_stop_time=""

function track() {
	#error case - no arguments passed
	if [ $# = 0 ]; then
		printf "track: This program requires an argument to be passed. See 'track --help'.\n"
	#start [label]
	elif [ $1 == 'start' ]; then
		#create file if it does not exist
		if [ ! -f $LOGFILE ]; then
			touch $LOGFILE
		fi

		#error case - other task is currently being tracked
		if [ $task_is_running == true ]; then
			printf "You may not track more than one task at a time.\nSee 'track status' to view your currently tracked task.\n"
		#error case - no label given started task
		elif [ $# -ne 2 ]; then
			echo "You need to give each tracked task a label. See 'track --help'\n"
		#(in this case, a label may have be more than one word)
		else
			task_is_running=true
			current_task=$2
			current_time=$(date)
			echo "Initialised tracking of task: $current_task"
			echo "Start time: $current_time"
			echo "START $current_time" >> $LOGFILE
			echo "LABEL $current_task" >> $LOGFILE
		fi
	#stop
	elif [ $1 == 'stop' ]; then
		if [ $task_is_running == false ]; then
			printf "No tasks are currently being tracked.\nSee 'track status' to view your currently tracked task.\n"
		else
			current_time=$(date)
			echo "Terminated tracking of task: $current_task"
			echo "End time: $current_time"
			echo "END $current_time" >> $LOGFILE
			echo "" >> $LOGFILE
			task_is_running=false
			current_task=""
		fi
	#status
	elif [ $1 == 'status' ]; then
		if [ $task_is_running == true ]; then
			echo "Current task: $current_task"
		else
			echo "No tasks are currently being tracked."
		fi
	#help
	elif [ $1 == '--help' ];
	then
		printf "This program helps you time track user defined tasks."
		printf "\nusage: track [--help] <command> [<args>]"
		printf "\nThe legal arguments are:"
		printf "\n	start [label]"
		printf "\n	stop"
		printf "\n	status"
		printf "\nThe program also generates a logfile."
		printf "\n"
	#error case - illegal argument(s)
	else
		printf "track: You tried to pass an illegal argument. See 'track --help'.\n"
	fi
}
