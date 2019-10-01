#!/usr/bin/env python
""" 4.3: Blurs an image by a 3x3 averaging kernel using python,
 and increasing compilation speed using numba.

Dependencies:
    numpy
    numba
    cv2
"""

import cv2
import numpy as np
from numba import njit

@njit
def _calc(src, dst):
    """ Private method that handles actual calculation.
    Sped up using njit - compiles as C code without accessing the Python interpreter.
    Does not return list due to call-by-reference of lists in python.
    """
    for h in range(0, dst.shape[0]):
        for w in range(0, dst.shape[1]):
            for c in range(0, dst.shape[2]):
                dst[h, w, c] = (src[h+1, w+1, c+1] +
                src[h, w+1, c+1] + src[h+2, w+1, c+1] +
                src[h+1, w, c+1] + src[h+1, w+2, c+1] +
                src[h, w, c+1]   + src[h, w+2, c+1] +
                src[h+2, w, c+1] + src[h+2, w+2, c+1]) / 9
    return dst

def blur(src):
    """ Blurs an image using pure python to calculate blur, compiled using numbas no-python JIT compilation.

    Args:
        src (int[][][]): The 3d matrix containing the original image.
    Returns:
        int[][][]: The 3d matrix of the blurred image result.
    """
    #set up source- and destination arrays
    dst = np.copy(src)
    src = np.pad(src, pad_width=1, mode='edge')

    #calculate blur
    _calc(src.astype("float"), dst)

    #return blurred image (as unsigned integers for OpenCV)
    return dst.astype("uint8")
