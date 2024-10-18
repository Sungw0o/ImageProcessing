import cv2
import numpy as np

# 100으로 채운 200x300 크기의 두 개의 행렬 생성
mat1 = np.full((200, 300), 100, np.uint8)
mat2 = np.full((200, 300), 100, np.uint8)

# 두 행렬을 0으로 초기화 (검정색 이미지)
mat1[:] = 0
mat2[:] = 0

# 창 생성 및 이미지 이동
cv2.namedWindow('window1')  # 첫 번째 창 생성
cv2.namedWindow('window2')  # 두 번째 창 생성

# 각 창의 위치를 설정
cv2.moveWindow('window1', 0, 0)  # 첫 번째 창을 (0, 0)에 이동
cv2.moveWindow('window2', 300, 200)  # 두 번째 창을 (300, 200)에 이동

# 각각의 창에 이미지를 표시
cv2.imshow('window1', mat1)
cv2.imshow('window2', mat2)

# 키 입력 대기 및 창 닫기
cv2.waitKey(0)
cv2.destroyAllWindows()
