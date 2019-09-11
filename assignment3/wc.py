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

import sys
import os

for file in sys.argv[1:]:
    if os.path.isfile(file):
        open_file = open(file, "r")
        num_of_lines = num_of_words = num_of_chars = 0

        for line in open_file.readlines():
            num_of_lines += 1
            num_of_words += len(line.replace("/n", "").split())
            num_of_chars += len(line)

        print(f"{num_of_lines} {num_of_words} {num_of_chars} {open_file.name}")
        open_file.close()
