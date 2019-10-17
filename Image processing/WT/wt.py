import numpy as np
import pywt
import cv2
import matplotlib.pyplot as plt

image = cv2.imread('cat.jpg')

gray_image = 1/3 * image[:,:,0] + 1/3 * image[:,:,1] + 1/3 * image[:,:,2]
m,n = gray_image.shape
gray_image = gray_image.astype('uint8')

plt.figure('二维小波一级变换')
coeffs = pywt.dwt2(gray_image, 'haar')
cA, (cH, cV, cD) = coeffs

# 将各个子图进行拼接，最后得到一张图
AH = np.concatenate([cA, cH], axis=1)
VD = np.concatenate([cV, cD], axis=1)
img = np.concatenate([AH, VD], axis=0)

# 显示为灰度图
plt.imshow(img,'gray')
plt.title('result')
plt.show()
