import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('cat.jpg')


gray_image = 1/3 * image[:,:,0] + 1/3 * image[:,:,1] + 1/3 * image[:,:,2]

#原图直方图
fig = plt.figure()
fig.add_subplot(211)
plt.hist(gray_image.ravel(),256)

MAX = 150
MIN = 20
img_min = np.min(gray_image)
img_max = np.max(gray_image)
tmp = np.where(gray_image < MAX , (gray_image - img_min) / (img_max - img_min) * (MAX - MIN) + MIN,gray_image)
fig.add_subplot(212)
cv2.imshow('tmp',tmp.astype('uint8'))
cv2.waitKey()
plt.hist(tmp.ravel(),256)
plt.show()