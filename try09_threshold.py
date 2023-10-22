import cv2

'''
阈值算法：
也叫二值算法，它把灰度分为黑与白，阈值之上是黑色，阈值之下是白色。
我们常说世界是复杂的，黑与白之间充满了灰色地带，但是在阈值算法眼里，世界是简单的，非黑即白。
它把连续分布的灰度范围切割为黑或者白。
'''
gray = cv2.imread("bookpage.jpg", cv2.IMREAD_GRAYSCALE)
ret, binary = cv2.threshold(gray, 10, 255, cv2.THRESH_BINARY)  # 阈值为10，最大灰度255
# cv2.threshold函数的返回值是一个元组，包含两个元素：一个是应用阈值后的二值化图像，另一个是阈值。
# 所以需要定义两个变量来分别存放这个阈值和图像。

binary_adaptive = cv2.adaptiveThreshold(
    gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 115, 1)

# 大金算法：在这个算法中我们不需要人为的确定阈值，它会自动击穿恰当的阈值，
# 使得分离出来的两个灰度分布差异最大化，它实际上是一个聚类分析算法
ret1, binary_otsu = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

cv2.imshow("gray", gray)
cv2.imshow("binary", binary)
cv2.imshow("adaptive", binary_adaptive)
cv2.imshow("otsu", binary_otsu)

cv2.waitKey()