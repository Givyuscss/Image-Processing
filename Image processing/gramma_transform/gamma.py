import cv2
import numpy as np


def gray(image):
    m,n,c = image.shape
    gray_image = np.zeros((m,n))
    for i in range(c):
        gray_image += 1/c * image[:,:,i]
    return gray_image


dark_image = gray(cv2.imread('dark_cat.jpg'))
bright_image = gray(cv2.imread('bright_cat.jpg'))

#gamma系数大于1会降低图像亮度，小于1会提升亮度
num = 5
gamma_blow1 = list(i/10 for i in range(5,10))
gamma_over1 = list(range(1,6))
gamma_img_bright = []#存放通过gamma变换加亮的dark_image
gamma_img_dark = []#存放通过gamma变换变暗的bright_image
for i in range(num):
    gamma_img_dark.append(255 * (np.array(bright_image)/255.0) ** gamma_over1[i])
    gamma_img_bright.append(255 * (np.array(dark_image)/255.0) ** gamma_blow1[i])

for i in range(num):
    cv2.imwrite('dark_cat_gamma=%.1f.jpg'%round(gamma_blow1[i],1), gamma_img_bright[i].astype('uint8'))
    cv2.imwrite('bright_cat_gamma=%d.jpg' %(gamma_over1[i]), gamma_img_dark[i].astype('uint8'))