import numpy as np
import cv2

# 도형을 그릴 때 사용할 색상 정의 이미지의 모든 픽셀 값을 흰색으로 만듬
blue, green, red = (255, 0, 0), (0, 255, 0), (0, 0, 255) #색상 선언
image = np.zeros((400, 600, 3), np.uint8) #3채널 컬러 영상 생성
image[:] = (255, 255, 255)  # 3채널 흰색

# 선을 그릴 두 좌표, 사각형을 그릴 두 좌표 와 영역을 지정
pt1, pt2 = (50, 50), (250, 150) # 좌표 선언
pt3, pt4 = (400, 150), (500, 50)
roi = (50, 200, 200, 100) # 사각형 영역 - 4원소 튜플

# 빨간 선과, 초록 색 선을 그림(안티 엘리어싱 적용)
cv2.line(image, pt1, pt2, red)
cv2.line(image, pt1, pt2, green, 3, cv2.LINE_AA) #계단 현상 감소선

# 4방향, 8방향으로 연결된 사각형을, 내부가 채워진 사각형을 그림
cv2.rectangle(image, pt3, pt4, blue, 3, cv2.LINE_4) # 4방향 연결선
cv2.rectangle(image, roi, red, 3, cv2.LINE_8) # 8방향 연결선
cv2.rectangle(image, (400, 200, 100, 100), green, cv2.FILLED) # 내부 채움

cv2.imshow('Line & Rectangle', image)
cv2.waitKey(0)
cv2.destroyAllWindows()