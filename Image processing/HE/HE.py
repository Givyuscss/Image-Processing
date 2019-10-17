import cv2
import matplotlib.pyplot as plt
import numpy as np

image = cv2.imread('tmp.jpg')

gray_image = 1/3 * image[:,:,0] + 1/3 * image[:,:,1] + 1/3 * image[:,:,2]

m,n = gray_image.shape
gray_image = gray_image.astype('uint8')
his = []
for i in range(256):
    his.append(np.sum(np.where(gray_image == i,1,0)) / (m * n))

c = np.cumsum(his)
LUT = np.round(c * 255)
new_image = np.zeros(m * n)
for i in range(n*m):
    new_image[i] = LUT[gray_image.ravel()[i]]
cv2.imwrite('res_tmp.jpg',new_image.reshape(m,n).astype('uint8'))

fig = plt.figure()
fig.add_subplot(121)
plt.hist(gray_image.ravel(),256)
fig.add_subplot(122)
plt.hist(new_image.ravel(),256)
plt.show()