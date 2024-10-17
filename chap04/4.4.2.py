import cv2
from Common.utils import print_matInfo
import matplotlib.pyplot as plt

title1, title2 = "color2gray", "color2color"
color2gray = cv2.imread("images/read_color.jpg", cv2.IMREAD_GRAYSCALE)
color2color = cv2.imread("images/read_color.jpg", cv2.IMREAD_COLOR)

if color2gray is None or color2color is None:
    raise Exception("영상 파일 읽기 에러")

print("행렬 좌표 (100, 100) 화소값")
print("%s %s" % (title1, color2gray[100, 100]))     # 한 화소값 표시
print("%s %s\n" % (title2, color2color[100, 100]))

# 이미지 정보 출력


print_matInfo(title1, color2gray)
print_matInfo(title2, color2color)

# 이미지 시각화
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(color2gray, cmap='gray')
plt.title(title1)
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(color2color, cv2.COLOR_BGR2RGB))
plt.title(title2)
plt.axis('off')

plt.show()