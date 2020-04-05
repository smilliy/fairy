# -*- coding: utf-8 -*-

import cv2
import numpy as np


imga = cv2.imread("atest.png")
imgb = cv2.imread("btest.png")

imgc = cv2.addWeighted(imga, 0.4, imgb, 0.6, 0)

cv2.imshow("imga+imgb", imgc)
cv2.waitKey(0)
cv2.destroyAllWindows()
