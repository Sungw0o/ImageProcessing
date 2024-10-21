# 마우스 이벤트 사용
import numpy as np
import cv2

def onMouse(event, x, y, flags, param): #이벤트 유형 , 좌표, 사용자 정의 파라미터
    if event == cv2.EVENT_LBUTTONDOWN:
        print("마우스 왼쪽 버튼 누르기")
    elif event == cv2.EVENT_RBUTTONDOWN:
        print("마우스 오른쪽 버튼 누르기")
    elif event == cv2.EVENT_RBUTTONUP:
        print("마우스 오른쪽 버튼 떼기")
    elif event == cv2.EVENT_LBUTTONDBLCLK:
        print("마우스 왼쪽 버튼 더블 클릭")


image = np.full((200,300), 255, np.uint8)

title1, title2 = "Mouse Event1", "Mouse Event2"
cv2.imshow(title1, image)
cv2.imshow(title2, image)

cv2.setMouseCallback(title1, onMouse) # 이벤트 발생하는 윈도우 이름, 콜백 함수, 이벤트 처리 함수로 전달할 추가적인 사용자 정의 인수
cv2.waitKey(0)
cv2.destroyAllWindows()