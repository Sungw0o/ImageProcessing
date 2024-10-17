import cv2
import numpy as np
import matplotlib.pyplot as plt

# 원본 영상과 로고 영상 읽기
image = cv2.imread("images/bit_test.jpg", cv2.IMREAD_COLOR)     # 원본 영상 읽기
logo  = cv2.imread("images/logo.jpg", cv2.IMREAD_COLOR)         # 로고 영상 읽기
if image is None or logo is None:
    raise Exception("영상 파일 읽기 오류 ")

# 로고 영상 이진화 (Thresholding)
_, masks = cv2.threshold(logo, 220, 255, cv2.THRESH_BINARY)
masks = cv2.split(masks)

# 전경 통과 마스크와 배경 통과 마스크 생성
fg_pass_mask = cv2.bitwise_or(masks[0], masks[1])       # 전경 통과 마스크
fg_pass_mask = cv2.bitwise_or(masks[2], fg_pass_mask)
bg_pass_mask = cv2.bitwise_not(fg_pass_mask)

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

cv2.imshow('backgorund', background);
cv2.imshow('forground', foreground);
cv2.imshow('dst',dst)
cv2.imshow('image',image)
cv2.waitKey()