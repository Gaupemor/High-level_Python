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
        
        modLines = []
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
            
            # if no more lines present in modified (take into account blank line)
            if modLine != '' and not modLine:
                output.write(f"- {line}\n")
                line = original.readline()
            # if not modified, add 0 in front of line
            elif line == modLine:
                # if 'leftover' modLines - lines have been added
                if modLines:
                    for m in modLines:
                        output.write(f"+ {m}\n")
                    modLines = []
                output.write(f"0 {line}\n")
                line = original.readline()
                modLine = modified.readline()
                
            #if line is in accumulated modified lines
            elif line in modLines:
                j = 0
                while modLines[j] != line:
                    m = modLines[j]
                    output.write(f"+ {m}\n")
                    j += 1
                output.write(f"0 {line}\n")
                for k in range(0, j):
                    modLines.pop(0)
                modLines.pop(0)
                line = original.readline()
                
            # OTHER MODIFICATIONS
            else:
                output.write(f"- {line}\n")
                line = original.readline()
                modLines.append(modLine)
                modLine = modified.readline()
                
        # if more added lines present in modified file
        while modLine:
            for m in modLines:
                output.write(f"+ {m}\n")
            output.write(f"+ {modLine}")
            modLine = modified.readline()            
    
# raise encountered exceptions through the parser
try:
    _apply()
except Exception as e:
    parser.error(e)