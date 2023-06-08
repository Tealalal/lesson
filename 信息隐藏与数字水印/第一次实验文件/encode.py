from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

def get_msg(msg):
    return msg.zfill(8)
def generate(msg): # 将信息转置为2进制。
    result=''
    for i in msg:
        if isinstance(i,int):
            result +=get_msg(bin(i)).replace('0b','')
        else:
            result+= get_msg(bin(ord(i)).replace('0b',''))
    return result

img=Image.open('flag.bmp')
tmp_msg='BUPT'
hide_msg=generate(tmp_msg)

# ascii=np.fromstring(tmp_msg,dtype=np.uint8)
# print('2020211919+林于翔+嵌入秘密信息的ASCII码为:'+str(ascii))
# print('2020211919+林于翔+嵌入秘密信息的二进制为:'+hide_msg)

width,height=img.size
length=len(hide_msg)
tmp=''
tmp2=''
count=0# 将信息隐藏到其最低位。
for i in range(0,width):
    if count == length:
        break
    for j in range(0,height):
        pixels=img.getpixel((i,j))
        a=pixels
        if count==length:
            break
        tmp+=str(a%2)
        a-=a%2+int(hide_msg[count])
        tmp2+=str(a%2)
        count+=1
        if count == length:
            img.putpixel((i, j), (a))
            break
        # tmp += str(b % 2)
        # b -= b % 2 + int(hide_msg[count])
        # tmp2 += str(b % 2)
        # count += 1
        # if count == length:
        #     img.putpixel((i, j), (a, b, c))
        #     break
        # tmp += str(c % 2)
        # c -= c % 2 + int(hide_msg[count])
        # tmp2 += str(c % 2)
        # count += 1
        if count == length:
            img.putpixel((i, j), (a))
            break
        # if count % 3 == 0:
        img.putpixel((i, j), (a))
img.save('encode.bmp')
plt.rcParams["font.sans-serif"] = "Arial Unicode MS"
plt.suptitle('2020211919+林于翔+载体图和携密图对比')
plt.subplot(121)
plt.imshow(mpimg.imread('flag.bmp'),cmap='gray'), plt.title('载体图像'), plt.axis('off')
plt.subplot(122)
plt.imshow(mpimg.imread('encode.bmp'),cmap='gray'), plt.title('携密图像'), plt.axis('off')
plt.show()






























