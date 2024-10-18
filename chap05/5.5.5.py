import numpy as np, cv2

# 난수 생성의 값 범위가 0 ~ 100 사이로 조정
m = np.random.rand(3,5) * 1000//10

# 행렬 축소 연산
# 열 방향으로 합계 계산
reduce_sum = cv2.reduce(m, dim=0, rtype=cv2.REDUCE_SUM) # 0 - 열방향 축소
# 행 방향으로 평균 계산
reduce_avg = cv2.reduce(m, dim=1, rtype=cv2.REDUCE_AVG) # 1 - 행방향 축소
# 열 방향으로 최댓값 계산
reduce_max = cv2.reduce(m, dim=0, rtype=cv2.REDUCE_MAX)
# 행 방향으로 최솟값 계산
reduce_min = cv2.reduce(m, dim=1, rtype=cv2.REDUCE_MIN)

print("[m1] = \n%s\n" %m)
print("[m_reduce_sum] =", reduce_sum.flatten())
print("[m_reduce_avg] =", reduce_avg.flatten())
print("[m_reduce_max] =", reduce_max.flatten())
print("[m_reduce_min] =", reduce_min.flatten())