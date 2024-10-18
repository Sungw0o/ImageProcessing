import cv2
import numpy as np

def onMouse(event, x, y, flags, param):
    global title
    # 두 개의 튜플을 더할 수 없다
    # if event == cv2.EVENT_LBUTTONDOWN:
    #     cv2.circle(image, pt, 5, 100, 1)
    # elif event == cv2.EVENT_RBUTTONDOWN:
    #     cv2.rectangle(image, pt, pt+(30, 30), 100, 2)
    #     cv2.imshow(title , image)
    pt = (x, y)  # 마우스 좌표를 pt로 설정
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(image, pt, 5, 100, 1)  # 왼쪽 클릭 시 원 그리기
        cv2.imshow(title, image)  # 이미지를 다시 갱신해 표시
    elif event == cv2.EVENT_RBUTTONDOWN:
        # 오른쪽 클릭 시 사각형 그리기
        cv2.rectangle(image, pt, (x + 30, y + 30), 100, 2)
        cv2.imshow(title, image)  # 이미지를 다시 갱신해 표시

image = np.ones((300, 300), np.uint8) * 255

title = "Draw event"
cv2.namedWindow(title)
cv2.imshow(title, image)
cv2.setMouseCallback(title, onMouse)
cv2.waitKey(0)
cv2.destroyAllWindows()