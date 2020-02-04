import numpy as np

def bob_deinterlace(img, flag):
    if flag == "TOP_FIELD_FIRST" or not flag:
        return bob_deinterlace_top_field_first(img)
    else:
        return img, img

def bob_deinterlace_top_field_first(img):
    frame1, frame2 = np.zeros(img.shape).astype(img.dtype), np.zeros(img.shape).astype(img.dtype)
    frame1[::2] = img[::2]
    frame1[1::2] = img[::2]
    frame2[::2] = img[1::2]
    frame2[1::2] = img[1::2]
    return frame1, frame2