import numpy as np, cv2


image = cv2.imread("images/minMax.jpg", cv2.IMREAD_GRAYSCALE)
if image is None:
    raise Exception("영상 파일 읽기 오류 발생")

# 원본 영상의 최솟값과 최댓값 계산
min_val, max_val, _, _ = cv2.minMaxLoc(image)

# 이미지 스케일 조정 (0~255 범위로 조정)
ratio = 255 / (max_val - min_val)
dst = np.round((image - min_val) * ratio).astype('uint8')
min_dst, max_dst, _, _ = cv2.minMaxLoc(dst)

# 최솟값, 최댓값 출력
print("원본 영상 최솟값= %d , 최댓값= %d" % (min_val, max_val))
print("수정 영상 최솟값= %d , 최댓값= %d" % (min_dst, max_dst))
cv2.imshow('image',image)
cv2.imshow('dst',dst)
cv2.waitKey(0)