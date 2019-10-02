## README selmafs assignments4

### PACKAGE
##### name
(directory)
```
blur_package
```

##### methods
```
blur_image([input file path], [output file path (optional)])
```
Reads an image from a given image file path as a 3d array,
blurs the image,
and optionally writes the blurred result to the given output file path.
The method also return an integer 3d array representing the blurred picture.

I: file path of image to blur
O: 3d array representing the blurred image

#### requirements (specified in setup.py)
- ```numpy```
- ```numba```
- ```opencv-python```
- ```pytest```

#### local installation
from the top direcory (assignment4, w/ setup.py and README.md)
```bash
$ pip install .
```

### useage (after installation)
see documentation for ```blur```
examples:
``` python
>>> import blur package
>>> blur_package.("img.jpg")
>>> blur_package.("img.jpg", "out.jpg")
```

#### RUN TESTS
using the testing framework ```pytest```
tests ```blur_image``` from the package
from the top direcory (assignment4, w/ setup.py and README.md)
```bash
$ pytest blur_package
```

#### RUNNING/USING OTHER SCRIPTS
all python scripts are located in the package directory,
but not all of them are used in the package (blur_1, blur_3, blur, blur_faces are excluded)

```
blur
```
command line user interface - see docstring for implementation and usage
example:
```bash
$ python blur.py -m 1 img.jpg out.jpg
```

### the rest
import as regular modules
(only ```blur_image```) is part of the package
see docstrings for more information about modules and methods
```
blur_1, blur_2, blur_3
```
example:
```python
>>> blur_[number].blur("img_array")
```
```
blur_faces
```
examples:
```
>>> blur_faces.blur_faces("img.jpg")
>>> blur_faces.blur_faces("img.jpg", "out.jpg")
```
```blur_faces``` uses around 60-90 seconds w/ ```beatles.jpg```

#### ADDITIONAL FILES/DIRECTORIES
```
blur_package
```
contains all python scripts except setup.py and __init__ to enable packaging
```
blur_package/tests
```
contains the test class test_blur.py for the package

```
blur_decorators
```
contains the decorator 'validimageIOfiles', 
used in blur.py and blur_package, 
raises an exception if input and output image file paths are not valid
```
__init__
```
for blur_package and blur_package/tests to enable packaging
