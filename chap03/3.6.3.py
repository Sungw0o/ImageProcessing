import numpy as np

np.random.seed(10) # 난수 생성시 고정된 시드값을 설정해 동일한 난수가 나오도록 설정
a = np.random.rand(2, 3) # 0,1 사이의 실수형 난수를 2 * 3 배열로 생성
b = np.random.randn(3, 2) # 표준 정규분포 (평균 0, 표준편차 1)를 따르는 난수를 3 * 2 배열로 생성
c = np.random.rand(6) # 0, 1 사이의 실수형 난수를 1차원 배열로 6개 생성
d = np.random.randint(1, 100, 6) # 1과 100 사이의 정수형 난수를 6개 생성
c = np.reshape(c, (2, 3)) # 1차원 배열 c를 2 * 3 형태의 2차원 배열로 재구성
d = d.reshape(2, -1) # 1차원 배열 d를 2차원 배열로 재구성

print('a 형태:', a.shape, '\n', a)
print('b 형태:', b.shape, '\n', b)
print('c 형태:', c.shape, '\n', c)
print('d 형태:', d.shape, '\n', d)

print('다차원 객체 1차원 변환 방법')
print('a =', a.flatten())

print('b =', np.ravel(b))

print('c =', np.reshape(c, (-1, )))
print('d =', d.reshape(-1, ))
