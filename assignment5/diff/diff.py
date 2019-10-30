#!/usr/bin/env python
""" 
Command-line interface that prints the details of how a given file
has been modified based on a given original file.
The program writes the results to a file called 'diff_output.txt'.

How to run:
    $ python diff.py [original file] [modified file]

Example:
    $ python diff.py org.txt mod.txt
"""

from argparse import ArgumentParser
import sys

# parser
parser = ArgumentParser(
    description="Checks if a given file has been modified compared to an original file")
    
# add arguments
parser.add_argument("original",
                    help="the original file to measure modifications by", metavar="original_file")
parser.add_argument("modified",
                    help="the modified file to check for divergences from the original", metavar="modified_file")
                    
# apply and get arguments
args = parser.parse_args()

# run program
def _apply():
    # open original file, modified file, and output file
    with open(args.original, 'r') as original, open(args.modified, 'r') as modified, open("diff_output.txt", 'w') as output:
        
        # read line from original and modified file
        line = original.readline()
        modLine = modified.readline()
        i = 0
        while line:
            # to account for EOF cases
            # (case original and modified strings are identical except for one containing a newline)
            line = line.rstrip()
            if modLine:
                modLine = modLine.rstrip()
            
            # if no more lines present in modified
            if not modLine:
                output.write(f"- {line}\n")
                line = original.readline()
            # if not modified, add 0 in front of line
            elif line == modLine:
                output.write(f"0 {line}\n")
                line = original.readline()
                modLine = modified.readline()
                
            # OTHER MODIFICATIONS
            else:
                if i == 0:
                    output.write(f"- {line}\n")
                    line = original.readline()
                    i += 1
                else:
                    ## TODO: handle cases i less than or greater than 0
                    print("something unexpected happened!")
                    print(f"original line: {line}")
                    print(f"modified line: {modLine}")
                    sys.exit(0)
                #not modified 0 before line
                #added + before line
                #deleted - before line
                #modified - deletion of org line, addition of mod line
                
        # if more added lines present in modified file
        while modLine:
            output.write(f"+ {modLine}")
            modLine = modified.readline()            
    
# raise encountered exceptions through the parser
try:
    _apply()
except Exception as e:
    parser.error(e)