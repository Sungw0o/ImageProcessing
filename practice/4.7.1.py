import numpy as np, cv2

# 흰색 배경 이미지 생성
image = np.zeros((300, 400, 3), np.uint8)
image[:] = (255, 255, 255)

# 두 점의 좌표
pt1, pt2 = (50, 130), (200, 300)

# 선 그리기 - 첫 번째 선
cv2.line(image, pt1, (100, 200), (0, 0, 0), 2)  # 선의 색상과 두께를 명시적으로 지정

# 선 그리기 - 두 번째 선 (세 번째 인수는 좌표, 네 번째 인수는 색상)
cv2.line(image, pt2, (100, 100), (100, 100, 100), 2)

# 사각형 그리기 - 두 가지 색상으로
cv2.rectangle(image, pt1, pt2, (255, 0, 255), 2)  # 보라색 사각형
cv2.rectangle(image, pt1, pt2, (0, 0, 255), 1)    # 빨간색 사각형

# 윈도우 설정 및 이미지 표시
title = "Line & Rectangle"
cv2.namedWindow(title)
cv2.imshow(title, image)
cv2.waitKey(0)
cv2.destroyAllWindows()
