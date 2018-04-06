import numpy as np


def cvt2grayscale_v1(img):
    grayImage = []
    for i in range(0, img.size // 3):
        luminance = int(0.3 * img[3 * i] + 0.59 * img[3 * i + 1] + 0.11 * img[3 * i + 2])
        grayImage.append(luminance)

    return np.array(grayImage)


def smooth_image_with_Gaussian_filter_v1(img):
    out = np.zeros((3,3))
    return out
