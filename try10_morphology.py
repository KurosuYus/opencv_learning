import cv2
import numpy as np


'''
图像的形态学算法：
本节主要学习腐蚀和膨胀
腐蚀（erosion）是一种数字图像处理中的基础操作，用于改变图像中物体的形状和大小。
腐蚀操作可以通过将图像中的每个像素点与其周围的像素进行比较，
并根据一定的规则来更新像素的值。
在腐蚀操作中，像素点的值通常会被其周围像素中最小（或最暗）的值所取代，
从而使物体的边缘变得更加平滑，并逐渐减小物体的尺寸。
这种操作可以用来去除图像中的小噪点、连接间断的图像区域以及分离相交的物体等。
腐蚀操作通常使用一个称为结构元素（structuring element）的小区域模板来定义比较规则。
结构元素可以是各种形状，如矩形、圆形、十字形等，它决定了腐蚀操作的效果和程度。
总结起来，腐蚀操作是数字图像处理中的一种基本操作，通过比较像素点与周围像素的值，
并根据一定规则更新像素的值，来改变图像中物体的形状和大小。
'''


gray = cv2.imread("./opencv_logo.jpg", cv2.IMREAD_GRAYSCALE)

# 本节操作基于二值化图像
_, binary = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY_INV)  # cv2.THRESH_BINARY_INV反向阈值因为原图背景是白色的，我们想要的是背景是黑色

# 定义一个操作核，它是一个5*5像素的正方形
kernel = np.ones((5, 5), np.uint8)  # 是 NumPy 库中的一个数据类型，它代表了无符号的 8 位整数（即 0 到 255 的整数）。

# 腐蚀
erosion = cv2.erode(binary, kernel)

# 膨胀
dilation = cv2.dilate(binary, kernel)

cv2.imshow("binary", binary)
cv2.imshow("erosion", erosion)
cv2.imshow("dilation", dilation)

cv2.waitKey()