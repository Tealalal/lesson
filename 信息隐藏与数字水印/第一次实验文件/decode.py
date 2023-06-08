from PIL import Image
from myencode import tmp_msg
img=Image.open('encode.bmp')
width,height=img.size
count=0
result=''
result1=''
length=len(tmp_msg)*8
for i in range(0,width):
    if count==length:
        break
    for j in range(0,height):
        pixel=img.getpixel((i,j))
        if count == length:
            break
        # if count%3==0:
        count+=1
        result1+=str(int(pixel)%2)
        if count==length:
            break
        # if count%3==1:
        #     count+=1
        #     result1+=str(int(pixel)%2)
        #     if count==length:
        #         break
        # if count%3==2:
        #     count+=1
        #     result1+=str(int(pixel)%2)
        #     if count==length:
        #         break
        if count==length:
            break
print("2020211919+林于翔提取出来的32位秘密信息为:"+result1)
for i in range(0,len(result1),8):
    result+=chr(int(result1[i:i+8],2))

print('2020211919+林于翔提取出来的秘密文本为:'+result)