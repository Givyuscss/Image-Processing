import cv2
import matplotlib.pyplot as plt
import numpy as np

image = cv2.imread('cat.jpg')

gray_image = 1/3 * image[:,:,0] + 1/3 * image[:,:,1] + 1/3 * image[:,:,2]

m,n = gray_image.shape
gray_image = gray_image.astype('uint8')
sub1 = []
sub2 = []


his = []
total = 0
e = 0
for i in range(256):
    num = np.sum(np.where(gray_image == i,1,0))
    total += num / (m * n)
    if total < 0.5:
        sub1.append(num)
        e = i + 1
    else:
        sub2.append(num)


c1 = np.cumsum(sub1) / np.sum(sub1)
c2 = np.cumsum(sub2) / np.sum(sub2)
LUT1 = np.round(c1 * e)
LUT2 = np.round(c2 * (255 - e) + e)

new_image = np.zeros(m * n)
for i in range(n * m):
    if gray_image.ravel()[i] < e:
        new_image[i] = LUT1[gray_image.ravel()[i]]
    else:
        new_image[i] = LUT2[gray_image.ravel()[i] - e]

cv2.imwrite('cat.jpg',new_image.reshape(m,n).astype('uint8'))

fig = plt.figure()
fig.add_subplot(121)
plt.hist(gray_image.ravel(),256)
fig.add_subplot(122)
plt.hist(new_image.ravel(),256)
plt.show()