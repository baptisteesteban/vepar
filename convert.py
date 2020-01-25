import numpy as np
from skimage import img_as_float, img_as_ubyte, io

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

def convert(img_filename):
    image_in = img_as_ubyte(io.imread(img_filename))
    image_out = convert_pgm(image_in)
    image_out = (image_out - image_out.min()) / (image_out.max() - image_out.min())
    image_out = img_as_ubyte(image_out)
    return image_out