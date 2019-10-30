## selmafs mandatory assignment 5

Tried to implement all bonus assignments except for 5.3 - favourite language syntax.

### 5.1 Syntax highlighting
Documentation in module docstring.

How to run from command line:
```bash
$ python highlighter.py [syntax file] [theme file] [source code file]
```

Example run:
```bash
$ python highlighter.py naython/naython.syntax naython/naython2.theme naython/hello.ny
```

Module methods:
```python
print_highlight(source_file, syntax, theme, print_only_matches=False)
```

### 5.2 Python syntax
Implemented:  
- Comments
- Function definitions
- Class definitions
- Strings
- Imports
- Special statements None, True, False
- Decorators
- Try/except
- For-loops
- While-loops
- if/elif/else blocks
- Certain symbols (e.g. + -) and certain 'words' (e.g. and, or, as, from)
  
Did not implement:
- Variable assignments
  
Files are located in python folder:  
- python.syntax
- python.theme
- python2.theme
- demo.py
  
Example run (from base assignment directory):
```bash
$ python highlighter.py python/python.syntax python/python.theme python/demo.py
```

### 5.3 Favourite language syntax
I did not implement this optional assigment.

### 5.4 grep
Implemented command line interface using argparse,  
with the possibility to pass more than one regex,  
and relies on the local module highlighter to avoid duplicate code.  
  
More help using ```$ python grep.py -h```.  
  
'demo' file used in directory grep: demo_grep.py (same as coloring_example.py) 
  
How to run:
```bash
$ python grep.py [--highlight|-hl] [soruce code file] [sequence of regex]
```

Example runs (from base assigment directory):
```bash
$ python grep.py grep/demo_grep.py a
$ python --highlight grep.py grep/demo_grep.py a b c
```
Output of first example (non-highlighted):  
```python
Prints a piece of text in a fancy way. What fancy means depends on the
   keyword argument code. Some possibilities are:
    0;3: italics
    0;5: blinking text (only sane default)
   these to get lovely things like flashing yellow text.
   start_code = "\033[{}m".format(code)
   print(start_code + text + end_code)
color_print("hei", code=sys.argv[1])
```

### 5.5 superdiff
Implemented command line interface using argparse.  
  
More help using ```$ python diff.py -h```.  
  
'demo' files used: demo_org.txt, demo_mod.txt, demo1_org.txt, demo1_mod.txt
  
Files:
- diff.py
  
How to run:
```bash
$ python diff.py [original file] [modified file]
```

Example run (using example described in assignment text):
```bash
$ python diff.py diff/demo_org.txt diff/demo_mod.txt
$ python diff.py diff/demo1_org.txt diff/demo1_mod.txt
```

### 5.6 Colouring diff
How to run:  
1. Run diff as described above
2. Run highlighter using diff syntax and theme files, and diff_output.txt

'demo' files used: diff_output.txt, demo_org.txt, demo_mod.txt