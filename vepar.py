#!/usr/bin/env python
import sys

import numpy as np
import matplotlib.pyplot as plt
from skimage import io, color, img_as_ubyte, img_as_float

def yuv_to_rgb(img):
    """
    From Video Processing and Communication (2001)
    """
    img = img.astype(np.int)
    res = np.zeros(img.shape).astype(np.float)
    res[:, :, 0] = 1.164 * (img[:, :, 0] - 16) + 1.596 * (img[:, :, 2] - 128)
    res[:, :, 1] = 1.164 * (img[:, :, 0] - 16) - 0.392 * (img[:, :, 1] - 128) - 0.813 * (img[:, :, 2] - 128)
    res[:, :, 2] = 1.164 * (img[:, :, 0] - 16) + 2.017 * (img[:, :, 1] - 128)
    return res

def convert_pgm(img):
    res = np.zeros((img.shape[0] * 2 // 3, img.shape[1], 3)).astype(np.uint8)
    res[:, :, 0] = img[:img.shape[0] * 2 // 3, :]
    
    U = img[img.shape[0] * 2 // 3:, :img.shape[1] //2]
    res[::2, ::2, 1] = U
    res[1::2, ::2, 1] = U
    res[::2, 1::2, 1] = U
    res[1::2, 1::2, 1] = U
    
    V = img[img.shape[0] * 2 // 3:, img.shape[1] //2:]
    res[::2, ::2, 2] = V
    res[1::2, ::2, 2] = V
    res[::2, 1::2, 2] = V
    res[1::2, 1::2, 2] = V
    
    return yuv_to_rgb(res)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage:", sys.argv[0], "input.pgm output.ppm", file=sys.stderr)
        exit(1)
        
    image_in = img_as_ubyte(io.imread(sys.argv[1]))
    image_out = convert_pgm(image_in)
    image_out = (image_out - image_out.min()) / (image_out.max() - image_out.min())
    image_out = img_as_ubyte(image_out)
    io.imsave("save.ppm", image_out)  
    
    plt.figure(figsize=(20, 10))
    plt.subplot(131)
    plt.imshow(image_out[:, :, 0], vmin=0, vmax=255, cmap="gray")
    plt.subplot(132)
    plt.imshow(image_out[:, :, 1], vmin=0, vmax=255, cmap="gray")
    plt.subplot(133)
    plt.imshow(image_out[:, :, 2], vmin=0, vmax=255, cmap="gray")
    plt.show()