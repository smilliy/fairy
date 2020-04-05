# -*- coding: utf-8 -*-

import cv2
import numpy as np


img = cv2.imread("test.png")


px = img[100, 100]
print(px)
blue = img[100, 100, 0]
print(blue)
print(img.item(10, 10, 2))
print(img.shape)
print(img.size)
print(img.dtype)
print(type(img))
cv2.imshow("image", img)

ball = img[30:130, 200:250]
img[50:150, 150:200] = ball
cv2.imshow("image1", img)

b, g, r = cv2.split(img)
print(b)
zeros = np.zeros(img.shape[:2], dtype="uint8")
img2 = cv2.merge([b, zeros, zeros])
cv2.imshow("image2", img2)

cv2.waitKey(0)
cv2.destroyAllWindows()