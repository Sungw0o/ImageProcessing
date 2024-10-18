import cv2

image = cv2.imread("images/color.jpg", cv2.IMREAD_COLOR)
if image is None:
    raise Exception("영상 파일 읽기 오류 발생")  # 예외 처리

# 첫 번째 차원은 높이, 두 번째 차원은 너비, 세 번째 차원은 채널(RGB 채널)
if image.ndim != 3:
    raise Exception("컬러 영상 아님")  # 3차원이 아니면 컬러 영상이 아님


# 채널 분리: 컬러 영상 --> 3채널 분리
bgr = cv2.split(image)

# bgr의 자료형을 출력
print("bgr 자료형:", type(bgr), type(bgr[0]), type(bgr[0][0][0]))
print("bgr 원소개수:", len(bgr))

cv2.imshow("image",image)
cv2.imshow("Blue channel", bgr[0]) # 파랑을 흑백으로 표시
cv2.imshow("Green channel", bgr[1]) # 초록을 흑백으로 표시
cv2.imshow("Red channel", bgr[2]) # 빨강을 흑백으로 표시
cv2.waitKey(0)
