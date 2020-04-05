# -*- coding: utf-8 -*-

import cv2
import numpy as np


img1 = cv2.imread("test.png")
cv2.imshow("img2", img1)
e1 = cv2.getTickCount()
for i in range(5, 49, 2):
    img1 = cv2.medianBlur(img1, i)
    print(i)
e2 = cv2.getTickCount()
t = (e2 - e1)/cv2.getTickFrequency()
print(t)
cv2.imshow("img", img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
