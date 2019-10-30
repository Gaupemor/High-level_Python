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
        
        # keep accumulated modified lines
        accumulated_lines = []
        # read line from original and modified file
        line = original.readline()
        modLine = modified.readline()
        
        while line:
            # to account for EOF cases
            # (case original and modified strings are identical except for one containing a newline)
            line = line.rstrip()
            if modLine:
                modLine = modLine.rstrip()
            
            # if no more lines present in modified (take into account blank line)
            if modLine != '' and not modLine:
                # assert that original line has been deleted
                output.write(f"- {line}\n")
                line = original.readline()
                
            # if not modified
            elif line == modLine:
                # if there are 'leftover' accumulated lines - lines have been added
                if accumulated_lines:
                    for m in accumulated_lines:
                        output.write(f"+ {m}\n")
                    accumulated_lines = []
                # write non-modified line
                output.write(f"0 {line}\n")
                line = original.readline()
                modLine = modified.readline()
                
            #if current line is in accumulated modified lines
            elif line in accumulated_lines:
                i = 0
                # add accumulated lines up until current line
                while accumulated_lines[i] != line:
                    m = accumulated_lines[i]
                    output.write(f"+ {m}\n")
                    i += 1
                # add non-modified line
                output.write(f"0 {line}\n")
                # remove added lines from accumulated lines
                for k in range(0, i):
                    accumulated_lines.pop(0)
                accumulated_lines.pop(0)
                line = original.readline()
                
            # else determine that line has been deleted
            else:
                output.write(f"- {line}\n")
                # read new lines and add current modified line to accumulated lines
                line = original.readline()
                accumulated_lines.append(modLine)
                modLine = modified.readline()
                
        # if more added lines present in modified file after done with original
        while modLine:
            # add accumulated lines and the modified line
            for m in accumulated_lines:
                output.write(f"+ {m}\n")
            output.write(f"+ {modLine}")
            modLine = modified.readline()            
    
# raise encountered exceptions through the parser
try:
    _apply()
except Exception as e:
    parser.error(e)