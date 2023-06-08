import math
import numpy as np
import cv2

def psnr(img1,img2):
    img1=np.float64(img1)
    img2=np.float64(img2)
    mse=np.mean((img1/1.0-img2/1.0)**2)
    if mse<1.0e-10:
        return 100
    PIXEL_MAX=255.0
    return 20 * math.log10(PIXEL_MAX/math.sqrt(mse))

img_gray=cv2.imread('c:/Users/13320/Desktop/LSB/man.bmp')
img_lsb=cv2.imread('c:/Users/13320/Desktop/LSB/mangraystego.bmp')
res=psnr(img_gray,img_lsb)
print(res)