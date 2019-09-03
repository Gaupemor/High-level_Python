##README assignment2 selmafs

I chose to support multiple word labels.
The label of a task will be assigned to all arguments after 'track start' collectively.

The program expects to find the directory for LOGFILE without tree traversal.
I understand that variables in all caps are supposed to be constants, but in my program, if no such environmental variable exists, the value of LOGFILE will be assigned to 'track_log.txt' in the working directory.

Added a --help command.
