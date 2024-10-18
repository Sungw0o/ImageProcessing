import numpy as np, cv2

# 그레이스케일 이미지의 밝기 값을 조정하는 작업을 수행
# 원본 이미지의 픽셀 값 범위를 0에서 255 사이로 재조정(정규화)하는 과정을 보여줌
image = cv2.imread("images/minMax.jpg", cv2.IMREAD_GRAYSCALE)
if image is None:
    raise Exception("영상 파일 읽기 오류 발생")

# 원본 영상의 최솟값과 최댓값 계산
min_val, max_val, _, _ = cv2.minMaxLoc(image)

# 이미지 스케일 조정 (0~255 범위로 조정)
# 이미지에서 실제로 존재하는 픽셀 값 범위를 나타냄
ratio = 255 / (max_val - min_val)
# 왼본 이미지의 각 픽셀 값에서 최솟값을 뺀 후 계산된 비율을 곱해 0 ~ 255 범위로 변환함
dst = np.round((image - min_val) * ratio).astype('uint8')
# 변환된 이미지의 최솟값과 최댓값 계산
min_dst, max_dst, _, _ = cv2.minMaxLoc(dst)

# 최솟값, 최댓값 출력
print("원본 영상 최솟값= %d , 최댓값= %d" % (min_val, max_val))
print("수정 영상 최솟값= %d , 최댓값= %d" % (min_dst, max_dst))
cv2.imshow('image',image)
cv2.imshow('dst',dst)
cv2.waitKey(0)

# 결론적으로 너무 어둡거나 대비가 낮은 이미지를 밝고 선명하게 조정하는 작업을 수행 함