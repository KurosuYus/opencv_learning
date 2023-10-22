import cv2
'''
前面的算法都用到了图像梯度，图像梯度就是图像的明暗变化
取图像的水平明暗变化和垂直明暗变化的，再取这两个变化的平方和就能得到梯度
与地理上的梯度类似，只不过地面的高低起伏变成了图像的明暗变化
'''
gray = cv2.imread("opencv_logo.jpg", cv2.IMREAD_GRAYSCALE)  # 这个参数可以直接读取灰度图

# 拉普拉斯算子，它大致对应图像的二阶导数
laplacian = cv2.Laplacian(gray, cv2.CV_64F)
'''
cv2.CV_64F：这是输出图像的深度（depth），用于指定输出图像的数据类型。在这里，cv2.CV_64F 表示输出图像将为 64 位浮点型数据。
表示无符号 8 位整数。
cv2.CV_16S 表示有符号 16 位整数。
cv2.CV_32F 表示单精度 32 位浮点数。
cv2.CV_64F 表示双精度 64 位浮点数。
'''

# Canny边缘检测
canny = cv2.Canny(gray, 100, 200)  # 100-200是梯度区间
'''
如果某个像素的梯度大于200，那么它周围的明暗变化剧烈，即判断它是一个边缘，
反之不是边缘。若是在区间之间，那么就要看它是否与已知的边缘像素相连，若是相连那么它也是边缘像素。

'''

cv2.imshow("gray", gray)
cv2.imshow("laplacian", laplacian)
cv2.imshow("canny", canny)
cv2.waitKey()