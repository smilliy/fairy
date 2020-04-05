# -*- coding: utf-8 -*-

import cv2


img = cv2.imread("test.png")
res1 = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
height, width = img.shape[:2]
res = cv2.resize(img, (2*width, 2*height), interpolation=cv2.INTER_CUBIC)

while 1:
    cv2.imshow("res", res)
    cv2.imshow("res1", res1)
    cv2.imshow("img", img)
    if cv2.waitKey(1) == 27:
        break
cv2.destroyAllWindows()
