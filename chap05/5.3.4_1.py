import cv2

# 원본 영상과 로고 영상 읽기
image = cv2.imread("images/bit_test.jpg", cv2.IMREAD_COLOR)     # 원본 영상 읽기
logo  = cv2.imread("images/logo.jpg", cv2.IMREAD_COLOR)         # 로고 영상 읽기
if image is None or logo is None:
    raise Exception("영상 파일 읽기 오류 ")

# 로고 영상 이진화 (Thresholding)
# 픽셀 값이 220 이상인 부분을 255 흰색으로 만들고 나머지는 0(검정색)으로 만드는 이진화 처리를 함
_, masks = cv2.threshold(logo, 220, 255, cv2.THRESH_BINARY)
# 이진화된 이미지를 BGR로 만들어 각 채널별 마스크를 생성함.
masks = cv2.split(masks)

# 전경 통과 마스크와 배경 통과 마스크 생성
# 각 채널에 논리합 연산을 적용해 전경(로고 부분)을 통과 시키는 마스크를 생성
fg_pass_mask = cv2.bitwise_or(masks[0], masks[1])       # 전경 통과 마스크
fg_pass_mask = cv2.bitwise_or(masks[2], fg_pass_mask)
# 전경 마스크의 반대 값을 취해 배경 마스크를 생성함. 배경이 1, 로고 부분이 0
bg_pass_mask = cv2.bitwise_not(fg_pass_mask) # 배경 통과 마스크

# 원본 이미지의 크기 (H,W) 로고 이미지의 크기 (h,w)를 구함
(H, W), (h, w) = image.shape[:2], logo.shape[:2]
x, y = (W-w)//2, (H-h)//2

# 관심 영역(roi) 지정
roi = image[y:y+h, x:x+w]

# 논리곱과 마스킹을 이용한 관심 영역 복사
foreground = cv2.bitwise_and(logo, logo, mask=fg_pass_mask)  # 로고의 전경 복사
background = cv2.bitwise_and(roi, roi, mask=bg_pass_mask)    # roi에 원본 배경만 복사

# 전경과 배경을 합성
dst = cv2.add(background, foreground)

# 합성된 영역을 원본 이미지에 복사
image[y:y+h, x:x+w] = dst

# 이미지의 관심 영역에서 로고가 들어갈 부분을 제외한 배경만을 복사한 이미지
cv2.imshow('backgorund', background);
# 로고 이미지에서 로고 부분만 추출한 이미지
cv2.imshow('forground', foreground);
# 백그라운드, 포어그라운드 합성 이미지
cv2.imshow('dst',dst)
# 최종적으로 원본 이밎에서 로고를 삽입한 형태의 이밎
cv2.imshow('image',image)
cv2.waitKey()

# 로고 이미지에서 배경을 제거하고, 원본 이미지의 특정 영역에 로고를 합성하는 작업을 수행함
# 마스킹을 통해 로고의 전경과 배경을 분리한 후, 원본 이미지와 합성하여 자연스럽게 삽입함.