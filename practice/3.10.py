import numpy as np
from collections import Counter

# 0 ~ 50 사이의 임의의 정수형 원소 500개 생성
arr = np.random.randint(0, 51, 500)

# 각 원소의 중복 횟수를 계산
counter = Counter(arr)

# 가장 중복이 많이 나온 원소 3개 추출
most_common_elements = counter.most_common(3)

# 결과 출력
for element, count in most_common_elements:
    print(f"원소: {element}, 중복 횟수: {count}")
