import cv2
import matplotlib.pyplot as plt
import numpy as np

# 300x300 크기의 검은색 이미지 생성
image1 = np.zeros((300, 300), np.uint8)
image2 = image1.copy()

# 이미지의 중심 좌표 계산
h, w = image1.shape[:2]
cx, cy = w // 2, h // 2

# image1: 중심에 원 그리기
cv2.circle(image1, (cx, cy), 100, 255, -1)

# image2: 왼쪽 절반을 흰색으로 채우기
cv2.rectangle(image2, (0, 0, cx, h), 255, -1)

# 비트 연산
image3 = cv2.bitwise_or(image1, image2)     # 원소 간 논리합
image4 = cv2.bitwise_and(image1, image2)    # 원소 간 논리곱
image5 = cv2.bitwise_xor(image1, image2)    # 원소 간 배타적 논리합
image6 = cv2.bitwise_not(image1)            # 행렬 반전

# Matplotlib으로 이미지 출력
plt.figure(figsize=(10, 6))

# 원본 이미지 1
plt.subplot(2, 3, 1)
plt.imshow(image1, cmap='gray')
plt.title('Image 1 (Circle)')
plt.axis('off')

# 원본 이미지 2
plt.subplot(2, 3, 2)
plt.imshow(image2, cmap='gray')
plt.title('Image 2 (Rectangle)')
plt.axis('off')

# 논리합
plt.subplot(2, 3, 3)
plt.imshow(image3, cmap='gray')
plt.title('Bitwise OR')
plt.axis('off')

# 논리곱
plt.subplot(2, 3, 4)
plt.imshow(image4, cmap='gray')
plt.title('Bitwise AND')
plt.axis('off')

# 배타적 논리합
plt.subplot(2, 3, 5)
plt.imshow(image5, cmap='gray')
plt.title('Bitwise XOR')
plt.axis('off')

# 반전
plt.subplot(2, 3, 6)
plt.imshow(image6, cmap='gray')
plt.title('Bitwise NOT')
plt.axis('off')

# 이미지 출력
plt.tight_layout()
plt.show()