import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img_c = mpimg.imread('test.bmp')
img = cv2.imread('test.bmp', cv2.IMREAD_GRAYSCALE)
img = cv2.resize(img,dsize=(512,512),fx=1,fy=1,interpolation=cv2.INTER_LINEAR)
cv2.imwrite('flag.bmp',img)

height,width = img.shape
img_dct = cv2.dct(np.array(img, np.float32))
for i in range(0,width):
     for j in range(0,height):
         if i > 300 or j > 300:
             img_dct[i,j] = 0
img_r = np.array(cv2.idct(img_dct), np.uint8)
cv2.imwrite('stego.bmp',img_r)

fig = plt.figure('DCT demo', figsize=(4,2))
plt.subplot(131)
plt.imshow(img, 'gray'), plt.title('Gray'), plt.axis('off')
plt.subplot(132)
plt.imshow(np.array(img_dct, np.uint8), cmap='hot'), plt.title('DCT mod'), plt.axis('off')
plt.subplot(133)
plt.imshow(img_r, 'gray'), plt.title('Recover mod'), plt.axis('off')
plt.tight_layout()
plt.show()
























