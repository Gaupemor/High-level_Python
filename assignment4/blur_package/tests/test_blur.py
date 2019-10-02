#!/usr/bin/env python
""" 4.6: Tests for the method 'blur_image'
 in the module 'blur_pkg' in the package 'blur_pkg'.

Tests are run using the pytest framework.

Dependencies:
    pytest
    numpy
    cv2
"""

import os
import numpy as np
import cv2
import blur_package as b


# CONSTANTS

# determines the height and width of the generated images
IMG_SIZE = 100
# path name for the temporary file to write generated images to
MOCK_FILE = "mock_blurred_image.jpg"

# HELP METHODS


def _set_seed():
    """ Private method that sets the random seed,
     so that the generated values are predictable.
    """
    np.random.seed(0)


def _generate_mock_image_file(tmp_path):
    """ Private method that arranges the image file
     for the unit tests testing the package.

    Generates a predictable random image (using a consistent random seed),
    writes the image to a temporary image file,
    and return the 3d generated image array read from the image file.

    Args:
        tmp_path (str): the temporary path in the pytest folder

    Yields:
        float[][][]: 3d array representing the generated image
    """

    # generate predictable random 3D image array
    generated_image = np.random.uniform(
                        low=1, high=255, size=(IMG_SIZE, IMG_SIZE, 3))

    # write to file so that the image is readable using 'blur_pkg.blur()'
    cv2.imwrite(MOCK_FILE, generated_image)

    # return the generated 3d image array
    # read from the image file for more correct result
    return cv2.imread(MOCK_FILE).astype("float")


def _blur_mock_image_file():
    """ Private method that blurs the given image array
     using the package 'blur_image()' method.

    Returns:
        int[][][]: 3d array representing the blurred image
    """
    return b.blur_image(MOCK_FILE)


def _destroy_mock_image_file():
    """ Private method that destroys the temporary file from the working directory.
    """
    if os.path.exists(MOCK_FILE):
        os.remove(MOCK_FILE)


# OBLIGATORY TESTS


def test_blur_pkg_max_value_of_image_decreased_after_blurring(tmp_path):
    """ Asserts that the max value of the array has decreased after blurring.
    """

    # Arrange

    # set random seed
    _set_seed()

    # generate image
    gen_img = _generate_mock_image_file(tmp_path)

    # blur image
    blurred_image = _blur_mock_image_file()

    # destroy temp file
    _destroy_mock_image_file()

    # Act

    # calculate max values
    pre_max_val = np.amax(gen_img)
    post_max_val = np.amax(blurred_image)

    # Assert

    # blurred image max smaller than original image max
    assert pre_max_val > post_max_val


def test_blur_pkg_correct_pixel_value(tmp_path):
    """ Asserts that a predictable random pixel has the
     expected colour value after blurring.
    """

    # Arrange

    # set random seed
    _set_seed()

    # generate image and pad
    gen_img = _generate_mock_image_file(tmp_path)
    gen_img = np.pad(gen_img, pad_width=1, mode='edge')

    # blur image
    blurred_image = _blur_mock_image_file()

    # destroy temp file
    _destroy_mock_image_file()

    # select predictable random pixel
    h = np.random.choice(blurred_image.shape[0])
    w = np.random.choice(blurred_image.shape[1])
    c = np.random.choice(blurred_image.shape[2])

    # Act

    # calculate actual and expected blur result for random pixel
    # (takes index shift from padding into account)
    actual_pixel_value = blurred_image[h, w, c]
    expected_pixel_value = (gen_img[h+1, w+1, c+1] +
                            gen_img[h, w+1, c+1] + gen_img[h+2, w+1, c+1] +
                            gen_img[h+1, w, c+1] + gen_img[h+1, w+2, c+1] +
                            gen_img[h, w, c+1] + gen_img[h, w+2, c+1] +
                            gen_img[h+2, w, c+1] + gen_img[h+2, w+2, c+1]) / 9
    expected_pixel_value = expected_pixel_value.astype("uint8")

    # Assert

    # actual pixel value equals expected pixel value
    assert actual_pixel_value == expected_pixel_value
