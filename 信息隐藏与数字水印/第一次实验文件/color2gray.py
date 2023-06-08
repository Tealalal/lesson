import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img_c = mpimg.imread('test.bmp')
img = cv2.imread('test.bmp', cv2.IMREAD_GRAYSCALE)
img = cv2.resize(img,dsize=(512,512),fx=1,fy=1,interpolation=cv2.INTER_LINEAR)
cv2.imwrite('flag.bmp',img)
# 设置字体的属性
plt.rcParams["font.sans-serif"] = "Arial Unicode MS"


plt.suptitle('2020211919+林于翔+彩色图和灰度图对比')
plt.subplot(121)
plt.imshow(img_c), plt.title('彩色图像'), plt.axis('off')
plt.subplot(122)
plt.imshow(img,'gray'), plt.title('灰色图像'), plt.axis('off')
plt.show()




































