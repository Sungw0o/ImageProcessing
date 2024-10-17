import numpy as np, cv2

image = cv2.imread("images/sum_test.jpg", cv2.IMREAD_GRAYSCALE)
#image = cv2.imread("images/sum_test.jpg", cv2.IMREAD_COLOR)
if image is None:
    raise Exception("영상 파일 읽기 오류 발생")

# 마스크 생성 및 관심 영역 설정
mask = np.zeros(image.shape[:2], np.uint8)
mask[60:160, 20:120] = 255  # 관심 영역을 지정한 후, 255를 할당

# 채널별 합 및 평균 계산
sum_value = cv2.sumElems(image)  # 채널별 합 구하기
mean_value1 = cv2.mean(image)    # 전체 평균 계산
mean_value2 = cv2.mean(image, mask)  # 마스크가 255인 영역의 평균 계산

# 결과 출력
print('sum_value 자료형:', type(sum_value), type(sum_value[0]))
print("[sum_value] = ", sum_value)
print("[mean_value1] = ", mean_value1)
print("[mean_value2] = ", mean_value2)
print()

# 평균과 표준편차 결과 저장
mean, stddev = cv2.meanStdDev(image)               # 전체 평균 및 표준편차
mean2, stddev2 = cv2.meanStdDev(image, mask=mask)  # 마스크가 255인 영역만 계산
print('mean 자료형:', type(mean), type(mean[0][0]))  # 반환 튜플의 원소는 ndarray
print("[mean] = "  , mean.flatten())                # 벡터 변환 후 출력
print("[stddev] = ", stddev.flatten())
print()

print("[mean2] = ",  mean2.flatten())
print("[stddev2] = ", stddev2.flatten())

cv2.imshow("image", image)
cv2.imshow("mask", mask)
cv2.waitKey(0)