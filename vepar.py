#!/usr/bin/env python
import sys

import numpy as np
import matplotlib.pyplot as plt
from skimage import io, color

def x4(X):
    res = np.zeros(2 * np.array(X.shape)).astype(np.uint8)
    res[::2, ::2] = X
    res[1::2, ::2] = X
    res[1::2, 1::2] = X
    res[::2, 1::2] = X
    return res

def yuv2rgb(img):
    res = np.zeros(img.shape).astype(np.uint8)

    Y = img[:, :, 0]
    U = img[:, :, 1]
    V = img[:, :, 2]

    res[:, :, 0] = Y + 1.4075 * (V - 128)
    res[:, :, 1] = Y - 0.3455 * (U - 128) - (0.7169 * (V - 128))
    res[:, :, 2] = Y + 1.7790 * (U - 128)
    
    return res

def pgm_to_ppm(input_img):
    if (input_img.ndim != 2):
        raise Exception("PGM2PPM: invalid shapes")
    (nrows, ncols) = input_img.shape
    res_img = np.zeros((nrows * 2 // 3, ncols, 3)).astype(np.uint8)
    # Get the channels
    Y = input_img[:nrows * 2 // 3, :]
    U = input_img[nrows * 2 // 3:, :ncols // 2]
    V = input_img[nrows * 2 // 3:, ncols // 2:]

    res_img[:, :, 0] = Y
    res_img[:, :, 1] = x4(U)
    res_img[:, :, 2] = x4(V)
    
    return yuv2rgb(res_img)

def main():
    if (len(sys.argv) < 3):
        print("Usage:", sys.argv[0], " input.pgm output.ppm")
        exit(1)

    input_img = io.imread(sys.argv[1]).astype(np.uint8)
    output_img = pgm_to_ppm(input_img)
    print(output_img.min(), output_img.max())
    io.imsave(sys.argv[2], output_img)
    exit(0)
        
if __name__ == "__main__":
    main()
