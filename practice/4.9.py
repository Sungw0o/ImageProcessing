import cv2
import numpy as np

# 600x400 크기의 검정색 배경을 가진 영상 생성
image = np.zeros((400, 600, 3), np.uint8)

# 빨간색 사각형을 그릴 좌표
top_left = (100, 100)  # 왼쪽 상단 좌표
bottom_right = (100 + 200, 100 + 300)  # 사각형의 크기 (200x300)

# 빨간색 (BGR: (0, 0, 255))
color = (0, 0, 255)

# 사각형 그리기 (image, 좌상단 좌표, 우하단 좌표, 색상, 두께 (-1은 내부 채우기))
cv2.rectangle(image, top_left, bottom_right, color, -1)

# 윈도우 생성 및 이미지 출력
cv2.namedWindow('Window', cv2.WINDOW_NORMAL)
cv2.imshow('Window', image)

cv2.waitKey(0)
cv2.destroyAllWindows()
