'''
这是均值滤波器测试
'''
import cv2

img = cv2.imread("plane.jpg")

gauss = cv2.GaussianBlur(img, (5, 5), 0)  # 这里的0是∑x，也就是∑由内核大小决定
gauss3 = cv2.GaussianBlur(img, (3, 3), 0)
gauss7 = cv2.GaussianBlur(img, (7, 7), 0)

median = cv2.medianBlur(img, 5)
median7 = cv2.medianBlur(img, 7)
median9 = cv2.medianBlur(img, 9)


cv2.imshow("img", img)
cv2.imshow("gauss", gauss)
cv2.imshow("gauss3", gauss3)
cv2.imshow("gauss7", gauss7)
cv2.imshow("median", median)
cv2.imshow("median7", median7)
cv2.imshow("median9", median9)

cv2.waitKey()