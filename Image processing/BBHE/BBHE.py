import cv2
import matplotlib.pyplot as plt
import numpy as np

image = cv2.imread('tmp.jpg')

gray_image = 1/3 * image[:,:,0] + 1/3 * image[:,:,1] + 1/3 * image[:,:,2]

print(gray_image.ravel().shape)
m,n = gray_image.shape
gray_image = gray_image.astype('uint8')
sub1 = []
sub2 = []
mean = int(np.mean(gray_image))
print(mean)
sumsub1 = np.sum(np.where(gray_image < mean,1,0))
sumsub2 = np.sum(np.where(gray_image >= mean,1,0))

for i in range(mean):
    sub1.append(np.sum(np.where(gray_image == i,1,0)) / sumsub1)
for i in range(mean,256):
    sub2.append(np.sum(np.where(gray_image == i,1,0)) / sumsub2)

c1 = np.cumsum(sub1)
c2 = np.cumsum(sub2)
LUT1 = np.round(c1 * mean)
LUT2 = np.round(c2 * (255-mean) + mean)
new_image = np.zeros(m * n)
for i in range(n * m):
    if gray_image.ravel()[i] < mean:
        new_image[i] = LUT1[gray_image.ravel()[i]]
    else:
        new_image[i] = LUT2[gray_image.ravel()[i] -  mean]

cv2.imwrite('res_tmp.jpg',new_image.reshape(m,n).astype('uint8'))

fig = plt.figure()
fig.add_subplot(121)
plt.hist(gray_image.ravel(),256)
fig.add_subplot(122)
plt.hist(new_image.ravel(),256)
plt.show()