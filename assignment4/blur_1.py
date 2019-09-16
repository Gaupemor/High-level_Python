import cv2
import numpy as np
import ntpath

def blur(srcPath):
    src = cv2.imread(srcPath).astype("float")
    dst = cv2.imread(srcPath)


    #add padding so can reach 0th and max-th pixels in h and w

    for h in range(1, src.shape[0] - 1):
        for w in range(1, src.shape[1] - 1):
            for c in range(0, src.shape[2]):
                dst[h, w, c] = (src[h, w, c] +
                src[h-1, w, c] + src[h+1, w, c] +
                src[h, w-1, c] + src[h, w+1, c] +
                src[h-1, w-1, c] + src[h-1, w+1, c] +
                src[h+1, w-1, c] + src[h+1, w+1, c]) / 9

    #extract path with ntpath
    cv2.imwrite(f"{srcPath}_blurred1.jpg", dst.astype("uint8"))
