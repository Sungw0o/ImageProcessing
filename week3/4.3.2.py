import numpy as np
import cv2
import matplotlib.pyplot as plt

# 색상 정의
olive, violet, brown = (128, 128, 0), (221, 160, 221), (42, 42, 165)
pt1, pt2 = (50, 200), (50, 260)  # 문자열 위치 좌표

# 흰색 배경 이미지 생성
image = np.zeros((300, 500, 3), np.uint8)
image.fill(255)

# 텍스트 추가
cv2.putText(image, "SIMPLEX", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, brown)
cv2.putText(image, "DUPLEX", (50, 130), cv2.FONT_HERSHEY_DUPLEX, 3, olive)
cv2.putText(image, "TRIPLEX", pt1, cv2.FONT_HERSHEY_TRIPLEX, 2, violet)
fontFace = cv2.FONT_HERSHEY_PLAIN | cv2.FONT_ITALIC  # 글자체 상수
cv2.putText(image, "ITALIC", pt2, fontFace, 4, violet)

# 이미지 표시 (BGR -> RGB 변환 후 matplotlib로 출력)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Put Text')
plt.axis('off')  # 축 숨김
plt.show()