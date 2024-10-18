import numpy as np, cv2

m = np.random.randint(0,100, 15).reshape(3,5)           # 임의 난수 생성

m_sort1 = cv2.sortIdx(m, cv2.SORT_EVERY_ROW)        # 행 기준으로 원소의 인덱스 정렬
m_sort2 = cv2.sortIdx(m, cv2.SORT_EVERY_COLUMN)     # 열 기준으로 원소의 인덱스 정렬
m_sort3 = np.argsort(m, axis=0)                         # 세로축을 기준으로 원소의 인덱스를 정렬

print("[m1] = \n%s\n" % m)
print("[m_sort1] = \n%s\n" % m_sort1)
print("[m_sort2] = \n%s\n" % m_sort2)
print("[m_sort3] = \n%s\n" % m_sort3)

# 정렬된 값 자체가 아닌 인덱스를 확인?