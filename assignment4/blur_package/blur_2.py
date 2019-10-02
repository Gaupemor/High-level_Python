#!/usr/bin/env python
""" 4.2: Blurs an image by a 3x3 averaging kernel using numpy arrays.

Dependencies:
    numpy
"""

import numpy as np


def _calc(src, dst):
    """ Private method that handles actual calculation.

    Calculates using numpy array-slicing,
    but loops through each channel seperatly.
    Does not return list due to call-by-reference of lists in python.
    """
    for c in range(0, dst.shape[2]):
        dst[:, :, c] = (src[1:-1, 1:-1, c+1] +
                        src[:-2, 1:-1, c+1] + src[2:, 1:-1, c+1] +
                        src[1:-1, :-2, c+1] + src[1:-1, 2:, c+1] +
                        src[:-2, :-2, c+1] + src[:-2, 2:, c+1] +
                        src[2:, :-2, c+1] + src[2:, 2:, c+1]) / 9

    return dst


def blur(src):
    """ Blurs an image using numpy arrays to calculate blur.

    Args:
        src (int[][][]): The 3d matrix containing the original image.
    Returns:
        int[][][]: The 3d matrix of the blurred image result.
    """
    # set up source- and destination arrays
    dst = np.copy(src)
    src = np.pad(src.astype("float"), pad_width=1, mode='edge')

    # calculate blur
    _calc(src.astype("float"), dst)

    # return blurred image (as unsigned integers for OpenCV)
    return dst.astype("uint8")
