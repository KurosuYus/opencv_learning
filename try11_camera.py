import cv2


capture = cv2.VideoCapture(0)  # 这个函数需要传入摄像头的序号

'''
与读取静态图片不同对于摄像头的采集是连续不断的，也就是说要循环读取每一帧的画面。
'''

# 由于不确定要循环多少次，所以采用死循环
while True:
    ret, frame = capture.read()
    cv2.imshow('camera', frame)
    key = cv2.waitKey(1)
    if key != -1:
        break


capture.release()