IN1130 selmafs
Assignment 4

PACKAGE
name: blur_package (directory)

methods:
blur_image([input file path], [output file path (optional)])
  Blurs an image from a given image file path,
  blurs the image,
  and optionally writes the blurred result to the given output file path.
  The method also return an integer 3d array representing the blurred picture.

  Requirements (specified in setup.py):
    numpy
    numba
    opencv-python
    pytest

  Local installation
  In top direcory (w/ setup.py and README.md)
    pip install .

  Useage (after installation):
  >>> import blur package
  >>> blur_package.("img.jpg")
  >>> blur_package.("img.jpg", "out.jpg")

RUN TESTS (requires pytest)
Tests 'blur_image' from the package
in the top directory:
  pytest blur_package

RUNNING/USING OTHER SCRIPTS
All python scripts are located in the package directory,
but not all of them are used in the package (blur_1, blur_3, blur, blur_faces)

  blur
  Command line user interface - see docstring for usage
  >>> python blur.py -m 1 img.jpg out.jpg

  import as regular modules
  (only 'blur_image') is part of the package

    blur_1, blur_2, blur_3
    >>> blur_x.blur("img_array")

    blur_faces
    >>> blur_faces.blur_faces("img.jpg")
    >>> blur_faces.blur_faces("img.jpg", "out.jpg")



ADDITIONAL FILES/DIRECTORIES

blur_package        all python scripts except setup.py and __init__ to enable packaging
blur_package/tests  contains the test class test_blur.py for the package

blur_decorators     contains the decorator 'validimageIOfiles'
                      used in blur.py and blur_package
                      raises an exception if input and output image file paths are not valid
__init__            for blur_package and blur_package/tests to enable packaging
