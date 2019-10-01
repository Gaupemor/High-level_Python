#!/usr/bin/env python
""" 4.5: Command line user interface for blurring images.

Args:
    Required:
        source_file: The file containing the image to blur.
        destination_file: The path to write the blurred product to.
    Optional:
        --help, -h (flag, optional): Prints help text.
        --module, -m {1, 2, 3} (optional):
            Determines which implementation of the three (3) modules to use -
            {blur_1, blur_2, blur_3}.

Examples:
    $ python blur.py -h
    $ python blur.py infile.jpg outfile.jpg
    $ python blur.py -m 1 infile.jpg outfile.jpg

For more information on usage, see the help text using the '--help' flag.

Dependencies:
    Local:
        blur_pkg
        blur_1
        blur_2
        blur_3
"""

from argparse import ArgumentParser
import blur_1, blur_2, blur_3
import blur_pkg as b

#list of modules for blurring: index of modules[] = index of module.choices[]
modules = [None, blur_1, blur_2, blur_3]

#parser
parser = ArgumentParser(description="image blurrer (by 3x3 pixel kernel average)")

#add arguments
parser.add_argument("src",
    help="path of image source file", metavar="source_file")
parser.add_argument("dest",
    help="path of image destination file", metavar="destination_file")
parser.add_argument("-m", "--module",
    type=int, help="choose implementation 1 (python), 2 (numpy) or 3 (python w/ numba) - set to 2 by default",
    choices=range(1, len(modules)), default=2)

#apply and get arguments
args = parser.parse_args()

#error handling and checking validity of source and destination file in blur_modules
#if not valid, ValueError is thrown by the parser
try:
    b.blur_image(args.src, args.dest)
except ValueError as v:
    parser.error(v)
