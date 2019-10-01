#!/usr/bin/env python
""" 4.6: Module containing the 'blur_pkg' package method 'blur(srcPath, dstPath)'.

This module contains the 'blur' method for the package (4.6).
Is also called by the console user interface 'blur.py' (4.5)
to handle reading from and writing to file.

Dependencies:
    cv2
    
    Local:
        blur_decorators
        blur_2
"""

import cv2
import blur_2 as b
from blur_decorators import validimageIOfiles

@validimageIOfiles
def blur_image(srcPath, dstPath=None):
    """ Blurs an image from a given image file.

    Uses the decorator 'validimageIOfiles' from 'blur_decorators'

    Args:
        srcPath (str): The path name for the image to blur.
        dstPath (str, optional): The path name to write the blurred image to.

    Returns:
        dst(int[][][]): 3d array containing the blurred image result.
    """
    #read source image (as float numbers)
    src = cv2.imread(srcPath).astype("float")

    #blur with the module blur_2
    dst = b.blur(src)

    #if destination path is given, write blurred image to file
    if dstPath is not None:
        cv2.imwrite(dstPath, dst)

    #return blurred image as 3d array of unsigned integers (parsed in blur_2)
    return dst
