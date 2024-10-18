import numpy as np, cv2

# 300 x 400 크기의 8비트 단일 채널
image = np.zeros((300, 400), np.uint8)
# 100은 회색에 해당함
image[:] = 100

title = 'Window'
# 윈도우를 100,200에 옮기고 생성
cv2.namedWindow(title, cv2.WINDOW_NORMAL)
cv2.moveWindow(title, 100, 200)
cv2.imshow(title, image)
cv2.waitKey(0)
cv2.destroyAllWindows()