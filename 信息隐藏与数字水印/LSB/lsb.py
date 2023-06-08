#lsb.py
#PIL图像处理库
from PIL import Image
#表格绘制库
import matplotlib.pyplot as plt
#数学库
import numpy as np

#图像的基本信息
img = Image.open("c:/Users/13320/Desktop/LSB/man.bmp")
width = img.size[0]
height = img.size[1]


#rgb彩色图像转灰度图
def rgb2gray(img_):
    img_ = img_.convert("L")
    return img_

#生成随机信息
def randomMsg(percent):
    if percent>0 and percent<=1:
        row = round(width * percent)
        col = round(height * percent)
        return np.random.randint(0,2,(col,row))
    else:
        raise Exception("传入的值必须属于(0,1]")

#将信息写入
def lsbWritein(img,msg):

    for y in range(len(msg)):
        for x in range(len(msg[0])):
            color = img.getpixel((x,y))
            temp = bin(color).replace('0b','')

            #不满足8bit长度的在高位补0
            for j in range(8-len(temp)):
                temp = '0' + temp

            temp = temp[0:7]+str(msg[y][x])
            img.putpixel((x,y),int(temp,2))
    return img

#主函数
def main():
    plt.figure("林于翔-2020211919")

    rt = 1

    img_gray = rgb2gray(img)
    martix_gray = np.array(img_gray)

    msg = np.array(randomMsg(rt))

    img_lsb = lsbWritein(img_gray,msg)
    martix_lsb = np.array(img_lsb)

    img_lsb.save('c:/Users/13320/Desktop/LSB/mangraystego.bmp')

    #表格绘制
    plt.subplot(121)
    plt.title("mangray.bmp")
    plt.hist(martix_gray.flatten(),bins=np.arange(0.5,257))
    plt.subplot(122)
    plt.title("mangraystego.bmp")
    plt.hist(martix_lsb.flatten(),bins=np.arange(0.5,257))
    plt.show()

main()
