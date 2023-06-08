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
m = [[]]

for i in range(8):
    m.append([])
    for j in range(8):
        p = img.getpixel((j,i))
        m[i].append(p[0])

result = ''
for i in range(8):
    for j in range(8):
        result += str(m[i][j])+' '
    result += '\n'
print("本人学号为2020211919，红色通道最左上角64个像素点值如下")
print(result)