import numpy as np, cv2

image = np.zeros((300, 400), np.uint8)

cv2.namedWindow('image', cv2.WINDOW_AUTOSIZE)
image[:] = 100  # 이미지 픽셀 값을 100으로 설정 (회색)

# 창의 이름을 첫 번째 인수로 전달해야 함
cv2.moveWindow('image', 500, 600)  # 'image' 창을 (500, 600) 위치로 이동

cv2.imshow('image', image)  # 창에 이미지 표시
cv2.waitKey(0)
cv2.destroyAllWindows()
