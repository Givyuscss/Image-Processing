import cv2
import numpy as np

image = cv2.imread('cat.jpg')
gray_image = 1/3 * image[:,:,0] + 1/3 * image[:,:,1] + 1/3 * image[:,:,2]#求和再取均值会出现噪声
reverse_image = 255 - np.array(gray_image)#存在小数，需要转为uint8模式

#cv2.imshow('a',reverse_image.astype("uint8"))
#cv2.waitKey()
cv2.imwrite('gray_cat.jpg',gray_image.astype("uint8"))
cv2.imwrite('reverse_gray_cat.jpg',reverse_image.astype("uint8"))