import numpy as np
import cv2

# 전역 변수 선언
image = np.zeros((300, 500), np.uint8)  # 300x500 크기의 검은 이미지 생성 (0으로 초기화)
title = "Trackbar & Mouse Event"  # 윈도우 제목
bar_name = "Brightness"  # 트랙바 이름
add_value = 0  # 추가 화소값 초기화 (밝기 조정값)

def onChange(value):  # 트랙바 콜백 함수
    global image, title, add_value  # 전역 변수 참조

    add_value = value - int(image[0][0])  # 트랙바 값과 영상 화소값 차분
    print("추가 화소값", add_value)
    image[:] = np.clip(image + add_value, 0, 255)  # 영상 밝기 조정 및 값 제한 (0 ~ 255) # 범위를 벗어나지 않게함
    cv2.imshow(title, image)  # 이미지 업데이트 후 다시 표시

def onMouse(event, x, y, flags, param):  # 마우스 콜백 함수
    global image, bar_name  # 전역 변수 참조

    if event == cv2.EVENT_RBUTTONDOWN:  # 오른쪽 버튼 클릭 시
        if image[0][0] < 246:  # 밝기가 246보다 작을 때만
            image[:] = image + 10  # 밝기를 10 증가
        cv2.setTrackbarPos(bar_name, title, image[0][0])  # 트랙바 위치를 이미지 밝기로 변경
        cv2.imshow(title, image)  # 이미지 업데이트 후 다시 표시

    elif event == cv2.EVENT_LBUTTONDOWN:  # 왼쪽 버튼 클릭 시
        if image[0][0] >= 10:  # 밝기가 10 이상일 때만
            image[:] = image - 10  # 밝기를 10 감소
        cv2.setTrackbarPos(bar_name, title, image[0][0])  # 트랙바 위치를 이미지 밝기로 변경
        cv2.imshow(title, image)  # 이미지 업데이트 후 다시 표시

# 초기 설정
image = np.zeros((300, 500), np.uint8)  # 300x500 크기의 검은 이미지 생성
title = "Trackbar & Mouse Event"  # 윈도우 제목
bar_name = "Brightness"  # 트랙바 이름

# 윈도우와 트랙바, 마우스 콜백 함수 설정
cv2.imshow(title, image)  # 윈도우에 기본 이미지 표시
cv2.createTrackbar(bar_name, title, image[0][0], 255, onChange)  # 트랙바 생성 및 콜백 함수 설정
cv2.setMouseCallback(title, onMouse)  # 마우스 콜백 함수 설정

cv2.waitKey(0)  # 키 입력 대기
cv2.destroyAllWindows()  # 모든 윈도우 닫기
