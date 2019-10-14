import sys
import re

# change to use argparse

# exit if wrong number of arguments
if len(sys.argv) != 4:
    raise TypeError("This module requires 3 additional arguments to highlighter.py")

syntax_file = sys.argv[1]
theme_file = sys.argv[2]
source_file = sys.argv[3]

def _setup_dicts():
    def _syntax():
        with open(syntax_file, "r") as s:
            try:
                pattern = re.compile(r'''((?:[^:"']|"[^"]*"|'[^']*')+)''')
                line = s.readline()
                while line:
                    #Split by ':', ignoring contents of strings, and then strip of trailing whitespaces and sting chars
                    entry = [e.strip('" ') for e in pattern.split(line)[1::2]]
                    syntax[entry[0]] = entry[1]
                    line = s.readline()
            except:
                raise IOError(f"The given syntax file {syntax_file} has faulty formatting.")
    def _theme():
        with open(theme_file, "r") as t:
            try:
                line = t.readline()
                while line:
                    entry = [e.strip() for e in line.split(":")]
                    theme[entry[0]] = entry[1]
                    line = t.readline()
            except:
                raise IOError(f"The given theme file {theme_file} has faulty formatting.")
    _syntax()
    _theme()


syntax = {}
theme = {}
_setup_dicts()

def _get_colour_code(name):
    return "\033[{}m".format(theme[name])


start_code = end_code = "\033[0m"
with open(source_file, "r") as source:
    line = source.readline()
    #iterate through each line
    while line:
        for k in syntax.keys():
            syntax_name = syntax[k]
            regex = re.compile(r'{}'.format(k)) # testing with the current syntax regex
            result = regex.search(line)
            if result is not None:
                indices = result.span()
                line = line[:indices[1]] + end_code + line[indices[1]:]
                line = line[:indices[0]] + _get_colour_code(syntax_name) + line[indices[0]:]

            #test if these actually work as intended
            #Special case 1: comments do not contain source code
            if syntax_name == "comment":
                break
        print(line.strip('\n'))
        line = source.readline()
