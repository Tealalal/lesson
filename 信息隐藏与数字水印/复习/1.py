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

plt.figure("2020211919+林于翔")
plt.subplot(221)
plt.imshow(img)
plt.title("2020211919+林于翔+彩色图像")
plt.subplot(222)
plt.imshow(img.getchannel("R"),'Reds')
plt.title("2020211919+林于翔+红色图像")
plt.subplot(223)
plt.imshow(img.getchannel("G"),"Greens")
plt.title("2020211919+林于翔+绿色图像")
plt.subplot(224)
plt.imshow(img.getchannel("B"),"Blues")
plt.title("2020211919+林于翔+蓝色图像")
plt.show()