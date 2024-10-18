import cv2
import numpy as np


# 마우스 콜백 함수
def onMouse(event, x, y, flags, param):
    if event == cv2.EVENT_RBUTTONDOWN:  # 오른쪽 마우스 버튼 클릭 시
        cv2.circle(image, (x, y), 20, (0, 0, 255), -1)  # 빨간색 원 그리기
        cv2.imshow('Mouse Event', image)

    elif event == cv2.EVENT_LBUTTONDOWN:  # 왼쪽 마우스 버튼 클릭 시
        top_left = (x - 15, y - 15)  # 사각형의 좌상단 좌표
        bottom_right = (x + 15, y + 15)  # 사각형의 우하단 좌표
        cv2.rectangle(image, top_left, bottom_right, (255, 0, 0), -1)  # 파란색 사각형 그리기
        cv2.imshow('Mouse Event', image)


# 500x500 크기의 흰색 배경 이미지 생성
image = np.ones((500, 500, 3), np.uint8) * 255

# 윈도우 생성
cv2.namedWindow('Mouse Event')
cv2.setMouseCallback('Mouse Event', onMouse)  # 마우스 콜백 함수 설정

# 화면에 이미지 표시
cv2.imshow('Mouse Event', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
