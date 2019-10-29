#!/usr/bin/env python
"""
Command-line interface that searches for matches to given regular expressions
in a given file containing source code.

Prints out every line containing a match.
If --highlight (-hl) flag is passed, the matches are coloured.

How to run:
    $ python grep.py [optional --highlight flag] [source file] [list of regular expressions] 
    
Examples:
    $ python grep.py source.lg a
    $ python grep.py source.lg a b c d
    $ python --highlight grep.py source.lg a b c d
    $ python -hl grep.py source.lg a b c d

Dependencies:
    Local modules:
        highlighter
"""

from highlighter import print_highlight
from argparse import ArgumentParser
import re
from itertools import cycle
from uuid import uuid4


# parser
parser = ArgumentParser(
    description="finds lines in file matching a given regular expression")
    
# add arguments
parser.add_argument("input",
                    help="the given file", metavar="input_file")
parser.add_argument("regex",
                    nargs='*',
                    help="the regular expression to search by",
                    metavar="regular_expression")
parser.add_argument("--highlight", "-hl",
                    action='store_true',
                    help="add this flag to colour the matches found")
                    
# apply and get arguments
args = parser.parse_args()

# perform program
def _apply():
    
    # DETERMINE COLOURS
    # uses a circular list object to iterate through all possible colours
    
    # no colour by default
    pool = cycle(["0"])
    # if to highlight, iterate through colours for each syntax
    if args.highlight:
        pool = cycle(["0;31", "0;32", "0;33", "0;34", "0;35", "0;36"])
        
    # CREATE DICTIONARIES FOR SYNTAX AND THEME
    
    syntax = {}
    theme = {}
    for r in args.regex:
        # creates a unique name for each regex entry w/uuid
        name = uuid4().hex[:6].upper()
        syntax[r] = name
        theme[name] = next(pool)
    
    # use the local highlighter module to print all matches using 
    print_highlight(args.input, syntax, theme, print_only_matches=True)

# print potential error message via parser
try:
    _apply()
except Exception as e:
    parser.error(e)