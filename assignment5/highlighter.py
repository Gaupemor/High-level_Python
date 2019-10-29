#!/usr/bin/env python
"""
5.1: Highlights the syntax of a file containing source code.

Prints out the coloured version of the source code using a given syntax- and theme file.

How to run:
    $ python highlighter.py [syntax file] [theme file] [source code file]
    
Example:
    $ python highlighter.py lang.syntax lang.theme source.lg
"""

import sys
import re

def print_highlight(source_file, syntax, theme, print_only_matches=False):
    """
    Prints out the coloured version of the source code using a given syntax and theme.
    
    Searches for each given syntax in source code,
    and colours them using a given theme.
    
    Arguments:
        source_file (text file):
            File containing the source code to highlight.
        syntax (dict of str: str):
            Contains the regular expression to search for syntax as key,
            and the name associated with the syntax as value.
        theme (dict of str: str):
            Contains the name associated with the syntax as key (relates to syntax value),
            and the colour escape code as value.
        print_only_matches (boolean) (optional):
            If true, prints only lines containing a regex match.
            False by default.
    """
    
    def get_colour_code(name):
        """ Returns:
                str: Colour code associated with syntax name.
        """
        
        return "\033[{}m".format(theme[name])
    
    # base colour escape code - no colour
    start_code = end_code = "\033[0m"
    
    # open file containing source code
    with open(source_file, "r") as source:
        
        line = source.readline()
        while line:
            regex_match_in_line = False;
            
            # Special case: comments do not contain source code
            comment_line = ""
            
            # for each given syntax entry
            for k in syntax.keys():
                
                # get syntax attributes and get regex result
                syntax_name = syntax[k]
                start_code = get_colour_code(syntax_name)
                regex = re.compile(r'{}'.format(k)) # test for regex match in current line
                result = regex.search(line)
                
                i = 0
                # while there is a regex match in line (in case multiple of same syntax present)
                while result:
                    regex_match_in_line = True
                    
                    # GET AND PREPARE MATCHED SLICE OF LINE
                    
                    # indexes of result
                    span = result.span()
                    # if there is no such result but still bypassed while, break
                    if not result.string or span[0] == span[1] == 0:
                        break
                    # account for index shift if multiple results in line
                    indices = (span[0] + i, span[1] + i)
                    
                    
                    # ADD HIGHLIGHTS
                    
                    # does not colour encasing whitespaces
                    if indices[1] != len(line) and line[indices[1] - 1] == ' ':
                        line = line[:indices[1] - 1] + end_code + line[indices[1] - 1:]
                    else:
                        line = line[:indices[1]] + end_code + line[indices[1]:]
                    if indices[0] != 0 and line[indices[0]] == ' ':
                        line = line[:indices[0] + 1] + start_code + line[indices[0] + 1:]
                    else:
                        line = line[:indices[0]] + start_code + line[indices[0]:]
                        
                        
                        
                    # SPECIAL SYNTAX CASES
                    
                    # Special case 1: comments do not contain source code
                    if syntax_name == "comment":
                        comment_line = line[indices[0]:]
                        line = line[:indices[0]]
                        
                    # Special case 2: colour each 'word' in string literals
                    if syntax_name == "string":
                        # get string literal
                        string_match = line[indices[0] + len(start_code):indices[1] + len(start_code)]
                        initial_string_length = len(string_match)
                        # get all whitespaces in string using regex
                        whitespaces_in_string = [(match.start(), match.end()) for match in re.finditer("\s", string_match)]
                        
                        if whitespaces_in_string:
                            j = 0
                            # for each whitespace, encase 'word' in highlight colour for string
                            for w in whitespaces_in_string:
                                string_match = string_match[:w[0] + j] + end_code + string_match[w[0] + j:w[1] + j] + start_code + string_match[w[1] + (w[1]-w[0]) + j - 1:]
                                j += len(start_code) + len(end_code)
                            # ensure highlight for first 'word' in string literal
                            if not string_match[1 + len(end_code)].isspace():
                                string_match = string_match[0] + start_code + string_match[1 + len(end_code):]
                            i += len(string_match) - initial_string_length
                            
                            # insert modified string to line
                            line = line[:indices[0] + len(start_code)] + string_match +  line[indices[0] + len(start_code) + initial_string_length:]
                    
                    # PREPARE NEXT ITERATION
                    # get new i shifted - to search rest of line for same regex
                    i = indices[1] + len(end_code) + len(start_code)
                    # get result from rest of line
                    result = regex.search(line[i:])
                    
            # Special case 1: comments do not contain source code
            # remove all other colour codes from comment
            if comment_line:
                # find colour escape code using regex
                colour_regex = re.compile(r'\033\[(.*?)m')
                result = colour_regex.search(comment_line[i:])
                i = 1
                # for each colour escape code within comment,
                # remove escape code and update comment line to print
                while result:
                    comment_line =  comment_line[:(result.span()[0]) + i] + comment_line[(result.span()[1] + i):]
                    i = result.span()[0]
                    result = colour_regex.search(comment_line[i:])
                comment_line = comment_line.rstrip() + "\033[0m"
                
            # print coloured line and get next line
            if not print_only_matches or regex_match_in_line:
                print(line.strip('\n') + comment_line.strip('\n'))
            line = source.readline()

if __name__ == "__main__":
    """
    Called if module is called from command line.
    
    Accepts syntax, theme and source code file as described above,
    creates a syntax and theme dictionary based of the input files
    and calls print_highlight().
    """
    
    # check if correct number of arguments given
    if len(sys.argv) != 4:
        raise TypeError("highlighter requires three (3) arguments: \n" +
            "$ python hightlighter.py [syntax file] [theme file] [source code file]")
    
    # input files
    syntax_file = sys.argv[1]
    theme_file = sys.argv[2]
    source_file = sys.argv[3]

    def setup_syntax():
        """Setup syntax dictionary based on given syntax file
        
        Returns:
            (dict of str: str): dictionary mapping regex to syntax name
            
        Raises:
            IOError: In case syntax file has faulty formatting or unable to read file.
        """
        syntax = {}
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
        return syntax
    def setup_theme():
        """Setup theme dictionary based on given theme file
        
        Returns:
            (dict of str: str): dictionary mapping syntax name to colour escape codes
            
        Raises:
            IOError: In case theme file has faulty formatting or unable to read file.
        """
        theme = {}
        with open(theme_file, "r") as t:
            try:
                line = t.readline().strip()
                while line:
                    entry = [e.strip() for e in line.split(":")]
                    theme[entry[0]] = entry[1]
                    line = t.readline()
            except:
                raise IOError(f"The given theme file {theme_file} has faulty formatting.")
        return theme

    print_highlight(source_file, setup_syntax(), setup_theme())
