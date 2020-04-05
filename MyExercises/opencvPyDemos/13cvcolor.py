# -*- coding: utf-8 -*-

import cv2


flags = [i for i in dir(cv2) if i.startswith('COLOR_')]
print(flags)

img1 = cv2.imread("test.png")
cv2.imshow("img1", img1)
img2 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
cv2.imshow("img2", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
