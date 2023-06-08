from PIL import Image
from function import stgPrb
import numpy as np
import matplotlib.pyplot as plt

#图像的基本信息
img = Image.open("man.bmp")
width = img.size[0]
height = img.size[1]
#rgb 彩色图像转灰度图
def rgb2gray(img):
    img = img.convert("L")
    return img

#生成 0/1 比特随机信息
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
            #不满足 8bit 长度的在高位补 0
            for j in range(8-len(temp)):
                temp = '0' + temp
            temp = temp[0:7]+str(msg[y][x])
            img.putpixel((x,y),int(temp,2))
    return img

#主函数
def main():
    img_gray = rgb2gray(img)
    #根据隐写率大小生成秘密信息，隐写率为 1
    rt = 1
    msg = randomMsg(rt)

    #lsb 隐写
    img_lsb = lsbWritein(img_gray,msg)
    img_lsb.save("c:/Users/13320/Desktop/LSB/mangraystego.bmp")

    # 确定隐写率为 1，对图片进行卡方分析,计算 p 值
    martix = np.array(img_lsb)
    p = stgPrb(martix[0:width, 0:height])
    print('2020211919+林于翔+卡方分析得到的P值为:'+str(p))

main()

