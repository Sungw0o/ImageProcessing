import numpy as np
import cv2

image = np.zeros((200,400), np.uint8) # 200 * 400 크기의 검은색 이미지 생성 unit8 형식
image[:] = 200 # 이미지의 모든 픽셀 값을 200으로 설정


title, title2 = 'Position1', 'Position2' # 창 제목을 정의
cv2.namedWindow(title, cv2.WINDOW_NORMAL) # 첫 번째 창 생성 (크기 조절 가능)
cv2.namedWindow(title2) # (기본 크기)
cv2.moveWindow(title, 150, 150) # 창을 화면의 특정 위치로 이동
cv2.moveWindow(title2, 400, 50) # 창을 화면의 특정 위치로 이동


cv2.imshow(title, image) # 첫 번째 창에 이미지 표시
cv2.imshow(title2, image) # 두 번째 창에 이미지 표시
cv2.waitKey(0)   # 키 이벤트 대기
cv2.destroyAllWindows() #  (아무 키나 눌렸다면) -> 열린 모든 창 닫힘