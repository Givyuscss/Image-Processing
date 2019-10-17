import cv2
import matplotlib.pyplot as plt
import numpy as np

image = cv2.imread('cat.jpg')

gray_image = 1/3 * image[:,:,0] + 1/3 * image[:,:,1] + 1/3 * image[:,:,2]

m,n = gray_image.shape
gray_image = gray_image.astype('uint8')

MAX = np.max(gray_image)
MIN = np.min(gray_image)

e = list(range(256))
AMBE = np.zeros(256)
images = []
for i in range(256):
    if i <= MIN or i >= MAX:
        images.append(gray_image)
        AMBE[i] = 255
        continue
    sub1 = []
    sub2 = []
    c1 = 0
    c2 = 0
    for j in range(256):
        if j < e[i]:
            sub1.append(np.sum(np.where(gray_image==j,1,0)))
        else:
            sub2.append(np.sum(np.where(gray_image==j,1,0)))
    if np.sum(sub1) != 0 and np.sum(sub2) != 0 :
        c1 = np.cumsum(sub1) / np.sum(sub1)
        c2 = np.cumsum(sub2) / np.sum(sub2)
        LUT1 = np.round(c1 * e[i])
        LUT2 = np.round(c2 * (255 - e[i]) + e[i])
        new_image = np.zeros(m * n)
        for k in range(n * m):
            if gray_image.ravel()[k] < e[i]:
                new_image[k] = LUT1[gray_image.ravel()[k]]
            else:
                new_image[k] = LUT2[gray_image.ravel()[k] - e[i] - 1]
        images.append(new_image)
        AMBE[i] = (np.abs((MAX-MIN-np.max(new_image)+np.min(new_image))))
    else:
        images.append(gray_image)
        AMBE[i] = 255

best = np.argsort(AMBE)[0]
cv2.imwrite('res_cat.jpg',images[best].reshape(m,n).astype('uint8'))

fig = plt.figure()
fig.add_subplot(121)
plt.hist(gray_image.ravel(),256)
fig.add_subplot(122)
plt.hist(images[best].ravel(),256)
plt.show()
