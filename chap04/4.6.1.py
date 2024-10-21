import cv2
import matplotlib.pyplot as plt

image  = cv2.imread("images/matplot.jpg", cv2.IMREAD_COLOR)
if image is None: raise Exception("영상 파일 읽기 에러")

# 이미지를 불러온 후 이미지의 높이와 너비를 가져옴
rows, cols = image.shape[:2] # 이미지 높이, 너비, 채널 수를 반환했음

# 이미지를 BGR에서 RGB로 변환 # 이미지의 색상 공간을 변환함
rgb_img = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
# 이미즈를 그레이 스케일로 변환 : 흑백 이미지 처리
gray_img = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

# 각각 서브플롯으로 나눠 출력함
# 새로운 그림을 생성 plt.figure()
fig = plt.figure(num=1, figsize=(3,4))
plt.imshow(image ), plt.title('figure1- original(bgr)')
# 축 범위, 간격 조정
plt.axis('off'), plt.tight_layout()

# 서브 플롯을 생성
fig = plt.figure(num=2, figsize=(6,4))
plt.suptitle( 'figure2- pyplot image display')
plt.subplot(1,2,1), plt.imshow(rgb_img)
plt.axis([0,cols, rows,0]), plt.title('rgb color')
plt.subplot(1,2,2), plt.imshow(gray_img, cmap='gray')
plt.title('gray_img2')
plt.show()