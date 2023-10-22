import cv2

img = cv2.imread("opencv_logo.jpg")
# 使用cv2读取文件

'''
对于opencv来说，存储一张图片等同于存储三种灰度图，它们被存储在opencv图像数据的
第三个维度上，灰度范围为0-255，opencv存储图像数据的顺序是B-G-R，当计算机需要
渲染这张图片时，计算机会依次取出图像数据中的三张灰度图，再把他们分别投影到显示器
的BGR的LED芯片上，从而渲染出彩色界面
'''

cv2.imshow("blue", img[:, :, 0])
cv2.imshow("green", img[:, :, 1])
cv2.imshow("red", img[:, :, 2])

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
'''
该参数下的cvtCOLOR函数会对三个彩色通道的图像做加权平均和平均
此时gray实际上描述了图像的明暗分布，如果它是相机cmos芯片上获得的图像，
我们也可以说它是cmos芯片上接收的光子分布图。
我们通常把获得的gray称为灰度图。
'''

cv2.imshow("gray", gray)

cv2.waitKey()
