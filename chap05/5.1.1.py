import cv2

# 컬러 영상을 불러옴
image = cv2.imread("images/flip_test.jpg", cv2.IMREAD_COLOR)

# x축 기준 상하 뒤집기, 좌우 뒤집기
x_axis = cv2.flip(image, 0)
y_axis = cv2.flip(image, 1)
xy_axis = cv2.flip(image, -1)
rep_image = cv2.repeat(image,1,2)
trans_image = cv2.transpose(image)
# 반복 복사 및 행렬 전치

## 각 행렬을 영상으로 표시
titles = ['image', 'x_axis', 'y_axis','xy_axis','rep_image','trans_image']
for title in titles:
    cv2.imshow(title, eval(title))

cv2.waitKey(0)