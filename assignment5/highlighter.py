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
                line = s.readline().strip()
                while line:
                    #finds the first ':' going backwards from end of line
                    colon_index = line.rfind(':')
                    syntax[line[1:colon_index-1]] = line[colon_index+1:].strip()
                    line = s.readline()
            except:
                raise IOError(f"The given syntax file {syntax_file} has faulty formatting.")
    def _theme():
        with open(theme_file, "r") as t:
            try:
                line = t.readline().strip()
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
            #in case of more than one match?
            i = 0
            while result:
                span = result.span()
                if not result.string or span[0] == span[1] == 0:
                    break
                indices = (span[0] + i, span[1] + i)
                start_code = _get_colour_code(syntax_name)
                line = line[:indices[1]] + end_code + line[indices[1]:]
                line = line[:indices[0]] + start_code + line[indices[0]:]
                i = indices[1] + len(end_code) + len(start_code)
                result = regex.search(line[i:])
                    
                #print(result, i, len(line), line[:-i])
                #Special case 1: comments do not contain source code
                if syntax_name == "comment":
                    break
            #test if these actually work as intended
            #Does not take into account multi-line strings or chars
        print(line.strip('\n'))
        line = source.readline()
