import numpy as np, cv2

# 300 x 400 크기의 8비트 단일 채널
image = np.zeros((400, 600, 3), np.uint8)
# 100은 회색에 해당함
image[:] = (255, 255, 255)
pt1, pt2 = (50, 100), (200, 300)

# 초록색 두께 5의 선 생성
cv2.line(image, pt1, pt2, (0, 255, 0), 5)
# 이미지, 사각형의 왼쪽 상단 좌표, 사각형의 오른쪽 하단 좌표, 두께 -1 (내부를 채움) , 그릴 때 사용할 선의 종류, 비트 시프트 (좌표 값은 2배로 해석)
cv2.rectangle(image, pt2, (300, 400), (0, 0, 255), -1, cv2.LINE_4, 1)


cv2.imshow("Line & Rectangle", image)
cv2.waitKey(0)
cv2.destroyAllWindows()