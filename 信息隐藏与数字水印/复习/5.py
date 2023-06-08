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

    plt.figure("2020211919+林于翔+原始图和携密图像对比")
    plt.subplot(121)
    plt.imshow(imgc)
    plt.title("原始图像")

    plt.subplot(122)
    plt.imshow(img)
    plt.title("携密图像")
    plt.show()
