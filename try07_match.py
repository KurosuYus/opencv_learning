import cv2
import numpy as np

img = cv2.imread("poker.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

template = gray[75:105, 235:265]  # 这里预先知道了菱形的位置并提取了出来

match = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF_NORMED)
# 传入待检测图像gray和模板template,cv2.TM_CCOEFF_NORMED是标准相关匹配算法
# 这个算法简单地说就是将待检测图像和模板都各自标准化再来计算匹配度这样可以保证匹配结果不受光照强度影响
locations = np.where(match >= 0.9)  # 找出匹配系数大于0.9的匹配点

# 接下来将模板图片的长和宽算出来
w, h = template.shape[0:2]
for p in zip(*locations[::-1]):  # 用于解压locations列表中的每一个元组，将 locations 中的横纵坐标反转
    x1, y1 = p[0], p[1]  # 由于opencv中是先列后行，所以要反转之后再发赋值
    x2, y2 = x1 + w, y1 + h  # 加上矩形的长和宽得到终点坐标
    cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)


cv2.imshow("img", img)
cv2.waitKey()

'''
这个匹配算法是对图像大小敏感的，小的菱形并没有被匹配标记
'''