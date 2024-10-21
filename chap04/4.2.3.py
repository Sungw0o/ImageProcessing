import numpy as np
import cv2

def onChange(value):							# 트랙바 콜백 함수
    global image, title                        # 전역 변수 참조

    add_value = value - int(image[0][0])       # 트랙바 값과 영상 화소값 차분
    print("추가 화소값", add_value)             # 행렬과 스칼라 덧셈 수행 (밝기 값을 조정)
    image[:] = image + add_value

    cv2.imshow(title, image)                   # 이미지 업데이트 후 다시 표시

# 영상 생성 (0으로 채우고 300x500, uint8)
image = np.zeros((300, 500), np.uint8)

title = "Trackbar Event"
cv2.namedWindow(title)                          # 창을 먼저 생성
cv2.imshow(title, image)                        # 기본 이미지를 먼저 표시

# 트랙바 생성
cv2.createTrackbar("Brightness", title, int(image[0][0]), 255, onChange) # 윈도우에 생성되는 트랙바 이름, 트랙바 부모 윈도우 이름
# 트랙바 슬라이더 위치 반영, 트랙바 슬라이더의 최댓값, 값이 변경될때 호출되는 콜백 함수

cv2.waitKey(0)
cv2.destroyAllWindows()
