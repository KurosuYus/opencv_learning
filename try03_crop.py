import cv2

img = cv2.imread("opencv_logo.jpg")

crop = img[10:170, 40:200]  # 列表中的第一个元素表示从第几列到第几列，第二个元素表示行

cv2.imshow("crop", crop)
cv2.waitKey()