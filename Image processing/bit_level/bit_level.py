import cv2
import numpy as np

image = cv2.imread('ex.jpg')

gray_image = 1/3 * image[:,:,0] + 1/3 * image[:,:,1] + 1/3 * image[:,:,2]

h,w = gray_image.shape
gray_image = gray_image.astype("uint8")
new_img = np.zeros((h,w,8))

for i in range(h):
    for j in range(w):
        n = str(np.binary_repr(gray_image[i,j],8))
        for k in range(8):
            new_img[i,j,k] = int(n[k]) * 255

for i in range(8):
    cv2.imwrite(('image_bite%d.jpg'%(8 - i)),new_img[:,:,i].astype("uint8"))
