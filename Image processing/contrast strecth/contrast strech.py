import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('cat.jpg')


gray_image = 1/3 * image[:,:,0] + 1/3 * image[:,:,1] + 1/3 * image[:,:,2]

#原图直方图
fig = plt.figure()
fig.add_subplot(311)
plt.hist(gray_image.ravel(),256)

#直方图平移
tmp1 = np.where(gray_image>30,gray_image - 30,0)
fig.add_subplot(312)
plt.hist(tmp1.ravel(),256)

#直方图平移后图像
cv2.imshow('a',tmp1.astype("uint8"))
cv2.waitKey()

#对比度拉伸
MAX = 255
MIN = 0
img_min = np.min(gray_image)
img_max = np.max(gray_image)
tmp2 = (gray_image - img_min) / (img_max - img_min) * (MAX - MIN) + MIN
fig.add_subplot(313)
plt.hist(tmp2.ravel(),256)

cv2.imshow('b',tmp2.astype("uint8"))
cv2.waitKey()
plt.show()


cv2.imwrite('linearization_cat.jpg',tmp1)
cv2.imwrite('contrast_strech_cat.jpg',tmp2)


