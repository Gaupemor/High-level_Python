#!/usr/bin/env python

"""Simple word count program for files - counts number of lines, words and characters.

    Note:
        Ignores all arguments that are not legal files.
        Requires Python v. 3.6 or later to enable f-string formatting

    Args:
        file(s): The file(s) to run word count on.

    Returns:
        List of strings in terminal, on the format
        [number of lines] [number of words] [number of characters] [file name]
        for each file.

    Example:
        >>> python wy.py file1.txt file2.txt directory1
        16 59 550 file1.txt
        2 25 112 file2.txt
"""

import sys, os

for file in sys.argv[1:]:
    if os.path.isfile(file):
        openFile = open(file, "r")
        numOfLines = numOfWords = numOfChars = 0

        for line in openFile.readlines():
            numOfLines += 1
            numOfWords += len(line.replace("/n","").split())
            numOfChars += len(line)

        print(f"{numOfLines} {numOfWords} {numOfChars} {openFile.name}")
        openFile.close()
