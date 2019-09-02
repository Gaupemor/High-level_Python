#!/bin/bash

task_is_running=false
current_task=""
all_tracked_tasks=()
current_start_time=""

function track() {

	#error case - no arguments passed
	if [ $# -eq 0 ]; then
		echo "track: This program requires an argument to be passed. See 'track --help'."

	#start [label]
	elif [ $1 == 'start' ]; then
		#LOGFILE
		#Set variable if environmental variable is not set
		if [ -z $LOGFILE ]; then
			LOGFILE="track_log.txt"
		#Create file if it does not exist
		elif [ ! -f $LOGFILE ]; then
			touch $LOGFILE
		fi

		#Attempt to add new task
		#error case - other task is currently being tracked
		if $task_is_running; then
			echo "You may not track more than one task at a time. See 'track status' to view your currently tracked task."
		#error case - no label given started task
		elif [ $# -lt 2 ]; then
			echo "Every tracked task must be assigned a label. See 'track --help'"
		else
			#Allow multiple word task labels - all args after 'start' part of task label
			start_arg=true;
			for i in $@; do
				if $start_arg; then
					start_arg=false
				else
					current_task+="$i "
				fi
			done
			#--------

			#get current time
			current_time=$(date)
			current_start_time=$(date +%s)

			#manage global variables
			task_is_running=true
			all_tracked_tasks+=("$current_task: currently tracking")

			#log in terminal and write to file
			echo "Initialised tracking of task: $current_task"
			echo "Start time: $current_time"
			echo "START $current_time" >> $LOGFILE
			echo "LABEL $current_task" >> $LOGFILE
		fi

	#stop
	elif [ $1 == 'stop' ]; then
		#error case - no task currently being tracked
		if ! $task_is_running; then
			echo "No tasks are currently being tracked. See 'track status' to view your currently tracked task."
		else
			#get current time
			current_time=$(date)
			current_end_time=$(date +%s)

			#log in terminal and write to file
			echo "Terminated tracking of task: $current_task"
			echo "End time: $current_time"
			echo "END   $current_time" >> $LOGFILE
			echo "" >> $LOGFILE

			#manage global variables
			#replace 'currently tracking' with elapsed time (formatted w/date command)
			unset 'all_tracked_tasks[${#all_tracked_tasks[@]} -1]'
			all_tracked_tasks+=("$current_task $(date -d@$(($current_end_time-$current_start_time)) -u +%H:%M:%S)")
			current_start_time=""
			task_is_running=false
			current_task=""
		fi

	#status
	elif [ $1 == 'status' ]; then
		if $task_is_running; then
			echo "Current task: $current_task"
		else
			echo "No tasks are currently being tracked. See 'track log' for completed tasks."
		fi

	#log
	elif [ $1 == 'log' ] ; then
		#in case no tasks to log
		if [ ${#all_tracked_tasks[@]} -eq 0 ]; then
			echo "No current or completed tasks to log."
		else
			#Iterated by indices - trouble w/ whitespaces in string when iterating by elements
			for i in $(seq 0 $((${#all_tracked_tasks[@]} - 1))); do
				echo "$(($i + 1))) ${all_tracked_tasks[$i]}"
			done
		fi

	#help
	elif [ $1 == '--help' ];
	then
		echo "This program helps you time track user defined tasks."
		echo "usage: track [--help] <command> [<args>]"
		echo "The legal arguments are:"
		echo "	start [label]"
		echo "				Starts tracking a new task."
		echo "				All tasks must have a label of one or more words."
		echo "				e.g. 'track start computing'"
		echo "				e.g. 'track start my new task'"
		echo "	stop"
		echo "				Stops currently tracked task."
		echo "	status"
		echo "				Shows currently tracked task, if there is one."
		echo "	log"
		echo "				Shows the elapsed time of all completed tasks."
		echo "	--help"
		echo "The program also generates a logfile."
		echo "The name of this logfile is specified by the environmental variable LOGFILE."
		echo "If no such variable is specified, a logfile named 'track_log.txt' will be created in the working directory."
		echo ""

	#error case - illegal argument(s)
	else
		echo "track: You tried to pass an illegal argument. See 'track --help'."
	fi
}
