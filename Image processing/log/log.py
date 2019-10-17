import cv2
import numpy as np
image = cv2.imread('gray_cat.jpg')
c = list(range(0,30,2))
log_image = []
for i in range(len(c)):
	log_image.append(c[i] * np.log(1 + image))

'''
for i in range(len(c)):
	cv2.imshow('gray_cat_c=%d'%(c[i]),log_image[i].astype("uint8"))
	cv2.waitKey( )
'''

for i in range(len(c)):
	cv2.imwrite('gray_cat_c=%d.jpg'%(c[i]),log_image[i].astype("uint8"))