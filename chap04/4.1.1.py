import numpy as np, cv2 # numpy, OpenCV 임포트


image = np.zeros((200,400),np.uint8)# 행렬 생성 200,400, 부호없는 8비트
image[:] = 200  # 밝은 회색(200) 바탕 생성
title1, title2 = "Position1", "Position2" # 윈도우 이름
cv2.namedWindow(title1, cv2.WINDOW_AUTOSIZE) # 윈도우 생성 및 크기 조정
cv2.namedWindow(title2)
cv2.moveWindow(title1, 150,150) # 위치를 (150, 150) (400, 50)으로 조정
cv2.moveWindow(title2, 400,50)

cv2.imshow(title1,image) # 행렬 원소 영상으로 표시
cv2.imshow(title2,image) # 행렬 원소 영상으로 표시
cv2.waitKey(0) # 키 이벤트 대기
cv2.destroyAllWindows() # 열린 모든 윈도우 파괴