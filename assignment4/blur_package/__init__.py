#!/usr/bin/env python
""" 4.6: Init file for the module 'blur_package' containing the 'blur_image' method.
"""

name = "blur_package"

import cv2
from blur_package.blur_2 import *
from blur_package.blur_decorators import validimageIOfiles

@validimageIOfiles
def blur_image(srcPath, dstPath=None):
    """ Blurs an image from a given image file, and optionally writes the blurred result to a given file.

    Args:
        srcPath (str): The path name for the image to blur.
        dstPath (str, optional): The path name to write the blurred image to.

    Returns:
        dst(int[][][]): 3d array containing the blurred image result.
    """
    #read source image (as float numbers)
    src = cv2.imread(srcPath).astype("float")

    #blur with the module blur_2
    dst = blur(src)

    #if destination path is given, write blurred image to file
    if dstPath is not None:
        cv2.imwrite(dstPath, dst)

    #return blurred image as 3d array of unsigned integers (parsed in blur_2)
    return dst
