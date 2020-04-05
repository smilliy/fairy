import cv2


def f1():
    events = [i for i in dir(cv2) if "Event" in i]
    print(events)


def f2():
    import numpy as np
    img = np.zeros((512, 512, 3), np.uint8)

    def _draw_cycle(event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDBLCLK:
            cv2.circle(img, (x, y), 100, (255, 0, 0), -1)
    cv2.namedWindow("image")
    cv2.setMouseCallback("image", _draw_cycle)
    while True:
        cv2.imshow("image", img)
        if cv2.waitKey(20) == 27:
            break
    cv2.destroyAllWindows()


def f3():
    import numpy as np
    img = np.zeros((512, 512, 3), np.uint8)
    print(img)
    drawing = False
    mode = True
    ix, iy = -1, -1

    def draw_circle(event, x, y, flags, param):
        global ix, iy, drawing
        if event == cv2.EVENT_LBUTTONDOWN:
            drawing = True
            ix, iy = x, y
        elif event == cv2.EVENT_MOUSEMOVE and flags == cv2.EVENT_FLAG_LBUTTON:
            if drawing:
                if mode:
                    cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)
                else:
                    cv2.circle(img, (x, y), 3, (255, 0, 0), -1)
        elif event == cv2.EVENT_LBUTTONUP:
            drawing = False
    cv2.namedWindow("image")
    cv2.setMouseCallback("image", draw_circle)
    while True:
        cv2.imshow("image", img)
        k = cv2.waitKey(1)
        if k == ord('m'):
            mode = not mode
        elif k == 27:
            break


f3()
