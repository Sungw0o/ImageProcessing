import numpy as np, cv2

src1 = np.array([1, 2, 3, 1, 2, 3], np.float32).reshape(2, 3) # 2x3 행렬 선언
src2 = np.array([1, 2, 3, 4, 5, 6], np.float32).reshape(2, 3)
src3 = np.array([1, 2, 1, 2, 1, 2], np.float32).reshape(3, 2) # 3x2 행렬 선언
alpha, beta = 1.0, 1.0

# 전치 행렬을 사용해 곱셈을 수행
dst1 = cv2.gemm(src1, src2, alpha, None, beta, flags=cv2.GEMM_1_T)
# 두 번째 함수를 전체 행렬를 사용해 곱셈
dst2 = cv2.gemm(src1, src2, alpha, None, beta, flags=cv2.GEMM_2_T)
dst3 = cv2.gemm(src1, src3, alpha, None, beta)

titles = ['src1','src1','src1','dst1','dst2','dst3']
for title in titles:
    print("[%s] = \n%s\n" % (title, eval(title)))

# 행렬 곱셈을 수행함