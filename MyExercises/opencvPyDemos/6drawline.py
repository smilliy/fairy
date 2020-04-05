import cv2
import numpy as np

img = np.zeros((888, 888, 3), np.uint8)
cv2.line(img, (0, 0), (511, 511), (255, 0, 0), 5)
cv2.rectangle(img, (384, 0), (510, 218), (0, 0, 255), 3)
cv2.circle(img, (447, 63), 63, (0, 0, 255), -1)
cv2.ellipse(img, (256, 256), (100, 50), 0, 0, 180, 255, -1)
pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)
pts = pts.reshape((-1, 1, 2))
cv2.polylines(img, pts, True, (255, 0, 0), 4, cv2.LINE_AA)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'OpenCV', (10, 500), font, 4, (255, 0, 0), 2)

cv2.namedWindow("example")
cv2.imshow("example", img)
cv2.waitKey(0)
cv2.destroyAllWindows()