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
    cv2

    Local:
        blur_decorators
        blur_1
        blur_2
        blur_3
"""

import cv2
from argparse import ArgumentParser
import blur_1, blur_2, blur_3
from blur_decorators import validimageIOfiles

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


@validimageIOfiles
def _blur_image(srcPath, dstPath, blur_module):
    """ Private method that reads image from file, blurs it, and writes to file.

    Args:
        srcPath (str): The path name for the image to blur.
        dstPath (str, optional): The path name to write the blurred image to.
    """
    #read source image (as float numbers)
    src = cv2.imread(srcPath).astype("float")

    #blur with the given module
    dst = blur_module.blur(src)

    #if destination path is given, write blurred image to file
    if dstPath is not None:
        cv2.imwrite(dstPath, dst)

    #return blurred image as 3d array of unsigned integers (parsed in blur_2)
    return dst


#error handling and checking validity of source and destination file in blur_modules
#if not valid, ValueError is thrown by the parser
try:
    _blur_image(args.src, args.dest, modules[args.module])
except ValueError as v:
    parser.error(v)
