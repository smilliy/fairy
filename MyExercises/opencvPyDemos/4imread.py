import cv2


def f1():
    img = cv2.imread("test.png", cv2.IMREAD_UNCHANGED)
    cv2.imshow("test", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def f2():
    """
    保存图像
    :return:
    """
    img = cv2.imread("test.png", cv2.IMREAD_UNCHANGED)
    cv2.imshow("test", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite("test1.png", img)


def f3():
    img = cv2.imread("test.png", cv2.IMREAD_GRAYSCALE)
    cv2.imshow("image", img)
    k = cv2.waitKey(0)
    print(k)
    if k == 27:
        cv2.destroyAllWindows()
    elif k == ord('s'):
        cv2.imwrite("test3.png", img)
        cv2.destroyAllWindows()


def f4():
    from matplotlib import pyplot as plt
    img = cv2.imread("test.png", cv2.IMREAD_ANYDEPTH)
    plt.imshow(img, cmap="gray", interpolation="bicubic")
    plt.xticks([])
    plt.yticks([])
    plt.show()


f4()
