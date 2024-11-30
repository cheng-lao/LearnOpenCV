import cv2 as cv
from matplotlib import pyplot as plt
"""
cv.IMREAD_COLOR 1 显示三色图
cv.IMREAD_GRAYSCALE 0 显示灰度图
cv.IMREAD_UNCHANGED 加载图像，包括alpha通道
"""
img = cv.imread("../../images/ambush_5_left.jpg", 1)

b, g, r = cv.split(img)
new_image = cv.merge([r, g, b])

cv.namedWindow("image", cv.WINDOW_AUTOSIZE)
cv.imshow('image-bgr', img)
cv.imshow("image-rgb", new_image)

# plt.imshow(img)
# plt.show()

k = cv.waitKey(0)

if k == ord('q'):
    # save image in annother place
    cv.imwrite("./temp.jpg", img)
    cv.destroyAllWindows()
elif k == 27:
    cv.destroyAllWindows()
    