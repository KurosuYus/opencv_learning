import cv2

img = cv2.imread("opencv_logo.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(gray, 500, 0.1, 10)  # 提取500个特征点，特征点的质量优于0.1，点之间的距离为10个像素
for corner in corners:  # 标记每一个特征点
    x, y = corner.ravel()  # x, y = corner.ravel()：这一行将 corner 变量进行了展平操作，ravel() 函数将 corner 数组转换为一维数组。然后，将一维数组的元素按顺序分别赋值给 x 和 y 两个变量。这意味着 x 和 y 分别保存角点的 x 坐标和 y 坐标。
    cv2.circle(img, (int(x), int(y)), 3, (255, 0, 255), -1)  #circle函数要求点的坐标为整数
# 通过以上步骤，循环遍历了角点列表中的每个角点，并在图像上绘制了一个紫色的圆来标记每个角点的位置。这样可以将角点可视化出来，以便后续处理或分析。

cv2.imshow("corner", img)
cv2.waitKey()

'''
以上代码可以标记出图像的特征点，从运行结果上可以看出标记出来的特征点都是图像的转角,
转角是一种最简单的图像特征，提取转角特征的算法都是非常高效的，所以它有非常广泛的应用，
比如在立体相机中，三维重建就需要非常大量的特征提取和匹配。
'''