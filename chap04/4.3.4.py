# 타원 및 호 그리기

import numpy as np
import cv2
import matplotlib.pyplot as plt

# 색상 지정
orange, blue, white = (0, 165, 255), (255, 0, 0), (255, 255, 255)

# 흰색 배경 이미지 생성
image = np.full((300, 700, 3), white, np.uint8)

# 타원 중심점 및 크기
pt1, pt2 = (180, 150), (550, 150)  # 타원 중심점
size = (120, 60)  # 타원 크기 (반지름 값)

# 타원의 중심점(2화소 원) 표시
cv2.circle(image, pt1, 1, 0, 2)
cv2.circle(image, pt2, 1, 0, 2)

# 타원 그리기
cv2.ellipse(image, pt1, size, 0, 0, 360, blue, 1)  # 전체 타원
cv2.ellipse(image, pt2, size, 90, 0, 360, blue, 1)
cv2.ellipse(image, pt1, size, 0, 30, 270, orange, 4)  # 호 그리기
cv2.ellipse(image, pt2, size, 90, -45, 90, orange, 4)

# matplotlib로 이미지 표시 (BGR -> RGB 변환 후)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Draw Eclipse & Arc')
plt.axis('off')  # 축 숨기기
plt.show()