import numpy as np
import cv2

# 도형을 그릴 때 사용할 색상 정의 이미지의 모든 픽셀 값을 흰색으로 만듬

# 파랑, 초록, 빨강 생성
blue, green, red = (255, 0, 0), (0, 255, 0), (0, 0, 255)
# 0으로 채우고 400, 600 3채널 컬러 , 부호없는 int 8비트
image = np.zeros((400, 600, 3), np.uint8)

# 배경을 흰색으로 만듬
image [:] = (255, 255, 255)

# 직선 좌표 (50, 50), (250, 150)
pt1, pt2 = (50, 50), (250, 150)
# 사각형 영역 (50, 200, 200, 100)
roi = (50, 200, 200, 100)

# 그냥 직선, 계단 현상 감소선
cv2.line(image, pt1, pt2, red)
cv2.line(image, pt1, pt2, green,3 ,cv2.LINE_AA) # 두께와 계단현상 감소선
# 4방향, 8방향, 내부 채움 사각형
cv2.rectangle(image, pt1, pt2, blue,3 ,cv2.LINE_4) # 두께 방향 연결선
cv2.rectangle(image, roi, blue,3 ,cv2.LINE_8)
cv2.rectangle(image,(400, 200, 100, 100), green, cv2.FILLED) # 내부 채움




cv2.imshow('Line & Rectangle', image)
cv2.waitKey(0)
cv2.destroyAllWindows()