#LSB卡方分析.py
from PIL import Image
from function import stgPrb
import numpy as np
import matplotlib.pyplot as plt
#图像的基本信息
img = Image.open("c:/Users/13320/Desktop/LSB/man.bmp")
width = img.size[0]
height = img.size[1]
#rgb彩色图像转灰度图
def rgb2gray(img):
    img = img.convert("L")
    return img

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
    plt.figure("pixel")
    #以嵌入率 100%进行 lsb 隐写
    rt = 1
    img_gray = rgb2gray(img)
    martix_gray = np.array(img_gray)
    msg = np.array(randomMsg(rt))
    img_lsb = lsbWritein(img_gray,msg)
    martix_lsb = np.array(img_lsb)

    #表格绘制，范围为 40-60
    x = range(40,61, 1)
    plt.subplots_adjust(hspace=0.3) # 调整子图间距
    plt.subplot(211)
    plt.title("img_gray")
    plt.hist(martix_gray.flatten(),bins=np.arange(40,61,1),rwidth=0.1,align='left')
    plt.xticks(x)

    plt.subplot(212)
    plt.title("img_lsb")
    plt.hist(martix_lsb.flatten(),bins=np.arange(40,61,1),rwidth=0.1,align='left')
    plt.xticks(x)

    plt.show()
main()
