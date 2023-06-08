import math
from scipy.stats import chi2
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np


plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

img = Image.open("lena.bmp")
imgc= img.copy()
width=img.size[0]
height = img.size[1]




def psnr(img1, img2):
    img1 = np.float64(img1)
    img2 = np.float64(img2)
    mse = np.mean((img1 / 1.0 - img2 / 1.0) ** 2)
    if mse < 1.0e-10:
        return 100
    PIXEL_MAX = 255.0
    return 20 * math.log10(PIXEL_MAX / math.sqrt(mse))


def generateMatrix(strs):
    ascii=""
    for i in strs:
        ascii +=str(ord(i))
    Matrix = [[]]

    for i in range(8):
        temp = bin(ord(strs[i])).replace('0b','').zfill(8)
        Matrix.append([])
        for j in range(8):
            Matrix[i].append(int(temp[j]))
    return Matrix

if __name__ == '__main__':
    msg=generateMatrix("BUPTSOCS")
    for i in range(8):
        for j in range(8):
           p = img.getpixel((j,i))
           p = list(p)
           p[0]=p[0] >> 1 << 1
           p[0]+=msg[i][j]
           p = tuple(p)
           img.putpixel((j,i),p)

    print("本人学号为2020211919，本人计算出来的PSNR值为%.2f"% psnr(img,imgc) )