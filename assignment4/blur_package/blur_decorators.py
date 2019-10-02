#!/usr/bin/env python
""" Module containing useful decorator methods for this package.
"""

import os
import mimetypes


def validimageIOfiles(func):
    """ Ensures validity of input and output image files
     when the arguments of the decorated function are image I/O files.

    Input image file is deemed valid if it is an existing, valid image file.
    Output image path (if given) is deemed valid
     if it has a legal image file extension.

    Args:
        func (function): Function to decorate.

    Returns:
        function: the decorated function

    Raises:
        ValueError: If the input or output image files are not valid.
    """

    def inner(*args, **kwargs):
        src_image_path = args[0]
        if len(args) == 1 or args[1] is None:
            dst_image_path = None
        else:
            dst_image_path = args[1]

        # src_image_path, dst_image_path
        legal_image_extensions = [".jpg", ".jpeg", ".jpx", ".png", ".bmp"]

        # source file - exists and is a valid image file
        if (not os.path.isfile(src_image_path)
                or "image" not in mimetypes.guess_type(src_image_path)[0]):
            raise ValueError(
                f"source image path is not an existing," +
                " valid image file: {src_image_path}")
        # destination file - has a valid image file extension
        elif (dst_image_path is not None
                and not any(dst_image_path.endswith(extension)
                            for extension in legal_image_extensions)):
            raise ValueError(
                f"destination image path does not have a" +
                " valid image file extension:\n{legal_image_extensions}")
        # if no exception to raise, return function
        else:
            return func(*args, **kwargs)

    return inner
