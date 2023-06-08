
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def get_msg(msg):
    return msg.zfill(8)
#作用：zfill()函数 方法在字符串的开头添加零（0），直到达到指定的长度（）
# 如果 len 参数的值小于字符串的长度，则不执行填充。

def StrToBinary(msg):#将信息转为2进制
    result=''
    for i in msg:
        if isinstance(i,int):
            result+=get_msg(bin(i).replace('0b',''))
        else:
            result+=get_msg(bin(ord(i)).replace('0b',''))
    return result
#ord表示将字符转为ascii码，bin表示将数字转为2进制，
# isinstance表示判断参数类型是不是给出的选择

img=Image.open('flag.bmp')
tmp_msg='BUPT'
hide_msg=StrToBinary(tmp_msg)

width,height=img.size
length=len(hide_msg)
tmp=''
tmp2=''
count=0 #将信息隐藏到最低位

for i in range(0,width):
    if count==length:
        break
    for j in range(0,height):
        if count==length:
            break
        pixels=img.getpixel((i,j))
        a=pixels
        tmp+=str(a%2)
        a+=a%2+int(hide_msg[count])
        tmp2+=str(a%2)
        count+=1
        if count==length:
            img.putpixel((i,j),a)
            break
        img.putpixel((i,j),a)

plt.rcParams["font.sans-serif"] = "Arial Unicode MS"
plt.suptitle('2020211919+林于翔+载体图和携密图对比')
plt.subplot(121)
plt.imshow(mpimg.imread('flag.bmp'),cmap='gray'), plt.title('载体图像'), plt.axis('off')
plt.subplot(122)
plt.imshow(mpimg.imread('encode.bmp'),cmap='gray'), plt.title('携密图像'), plt.axis('off')
plt.show()