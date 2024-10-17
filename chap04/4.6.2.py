import numpy as np
import matplotlib.pyplot as plt

# 보간이란 이미지 확대, 축소시 새로운 픽셀 값을 기존 픽셀로 부터 계산 (늘릴 때 빈 공간을 채우는 것)
# 그대로, 가까운 픽셀 보정, 선형 보간법 (인접 4개 픽셀 기준으로 계산)
# 16개의 인접 픽셀 기준으로 삼차 보간, 16차 스플라인 보간, 36차 스플라인 보간
methods = ['none', 'nearest', 'bilinear', 'bicubic', 'spline16', 'spline36' ]
grid = np.random.rand(5, 5)

# 2행 3열의 서브플롯을 생성 총 6개 각 서브플롯에 서로 다른 보간 방법을 적용하여 이미지를 표시
fig, axs = plt.subplots(nrows=2, ncols=3, figsize=(8, 6))

# 서브플롯과 보간 방법을 동시에 순회
# 각 서브플롯에 지정된 보간 방법을 사용해 이미지를 표시
for ax, method in zip(axs.flat, methods):
    ax.imshow(grid, interpolation=method, cmap='gray')
    ax.set_title(method)
plt.tight_layout(), plt.show()