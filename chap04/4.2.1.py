# 키 이벤트 사용

import numpy as np
import cv2

switch_case = {
    # ord() 함수 문자 -> 아스키 코드 변환
    ord('a'): "a키 입력",
    ord('b'): "b키 입력",
    0x41: "A키 입력",
    int('0x42',16): "B키 입력", # 0x42 (16진수) -> 10진수 변환
    2424832: "왼쪽 화살표키 입력",
    2490368: "윗쪽 화살표키 입력",
    2555904: "오른쪽 화살표키 입력",
    2621440: "아래쪽 화살표키 입력",
}

image = np.ones((200, 300), np.float32)         # 원소값 1인 행렬 생성 (200,300) float 32비트
cv2.namedWindow("keyboard Event")
cv2.imshow("keyboard Event", image)# 윈도우 이름 "keyboard Event"

while True:
                                # 무한반복
    key =cv2.waitKey(100)             # 100ms 동안 키 입력 대기
    if key == 27: break               # esc 누르면 종료

    try:
        result = switch_case[key]
        print(result)
    except KeyError:
        result = -1

cv2.destroyAllWindows()