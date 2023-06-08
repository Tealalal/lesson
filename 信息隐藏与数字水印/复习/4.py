import math
from scipy.stats import chi2
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np


plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

img = Image.open("lena.bmp")
width=img.size[0]
height = img.size[1]

def generateMatrix(strs):


    ascii=""
    for i in strs:
        ascii +=str(ord(i))

    print(strs+"的ASCII是"+ascii)

    Matrix = [[]]

    for i in range(8):
        temp = bin(ord(strs[i])).replace('0b','').zfill(8)
        Matrix.append([])
        for j in range(8):
            Matrix[i].append(int(temp[j]))
    return Matrix

if __name__ == '__main__':
    msg=generateMatrix("BUPTSOCS")
    m = [[]]
    for i in range(8):
        m.append([])
        for j in range(8):
           p = img.getpixel((j,i))
           p = list(p)
           p[0]=p[0] >> 1 << 1
           p[0]+=msg[i][j]
           p = tuple(p)
           img.putpixel((j,i),p)
           m[i].append(p[0])


    result = ''
    for i in range(8):
        for j in range(8):
            result += str(m[i][j]) + ' '
        result += '\n'
    print("本人学号为2020211919，隐写图像红色通道最左上角64个像素点值如下")
    print(result)
