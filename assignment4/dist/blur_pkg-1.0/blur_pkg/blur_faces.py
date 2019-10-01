#!/usr/bin/env python
""" 4.7: Blurs faces beyond recognition.

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
def blur_faces(srcPath, dstPath=None):
    """ Blurs front-facing faces recognized by the Haar cascade facial recognition algorithm,
    and displays the result.

    Uses the decorator 'validimageIOfiles' from 'blur_decorators'

    Args:
        srcPath (str): The path name for the image to blur.
        dstPath (str, optional): The path name to write the blurred image to.
    """
    image = cv2.imread(srcPath)
    faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

    def _faces():
        """ Private method searching for faces in image using Haar cascade.

        Returns:
            (int, int, int, int)[]: array containing coordinates for the detected faces.
        """
        return faceCascade.detectMultiScale(
            image,
            scaleFactor=1.025,
            minNeighbors=5,
            minSize=(30, 30)
        )

    #find faces
    faces = _faces()

    #print the number of faces found in the image by the face finder to console
    print(f"Found {len(faces)} faces.")

    #continue blurring until no faces in picture are recognizable (as faces)
    while len(faces) is not 0:
        for(x, y, w, h) in faces:
            #gets subsection containing face
            this_face = image[y:y+h, x:x+w]
            #blur subsection
            this_face = b.blur(this_face)
            #replace subsection of the original image with the blurred subsection
            image[y:y+h, x:x+w] = this_face

        #attempt to find faces in the blurred image
        faces = _faces()

    #if destination path is given, write blurred image result to file
    if dstPath is not None:
        cv2.imwrite(dstPath, image)

    #display result
    cv2.imshow("Result", image)
    cv2.waitKey(0)
