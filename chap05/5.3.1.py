import numpy as np, cv2

# 3 * 6 크기의 모든 요소가 10인 행렬 생성
m1 = np.full((3, 6), 10, np.uint8)			# 단일 채널 생성 및 초기화

# 3 * 6 크기의 모든 요소가 50인 행렬 생성
m2 = np.full((3, 6), 50, np.uint8)

m_mask = np.zeros(m1.shape, np.uint8)		# 마스크 생성

# 4번째 열부터 끝까지 마스크 값을 1로 설정해, 해당 영역이 연산에 적용되도록 함. 마스크가 1인 부분에만 연산 적용
m_mask[ :, 3: ] = 1							# 관심 영역을 지정한 후, 1을 할당

m_add1 = cv2.add(m1, m2)                    # 행렬 덧셈
m_add2 = cv2.add(m1, m2, mask=m_mask)       # 관심 영역만 덧셈 수행

# 행렬 나눗셈 수행
m_div1 = cv2.divide(m1, m2)   # 정수 나눗셈 모든 값이 0
m1 = m1.astype(np.float32)        # m1을 실수형으로 변환
m2 = np.float32(m2)             # m2를 실수형으로 변환
m_div2 = cv2.divide(m1, m2)   # 실수 나눗셈 모든 값이 0.2

titles = ['m1', 'm2', 'm_mask','m_add1','m_add2','m_div1', 'm_div2']
for title in titles:
    print("[%s] = \n%s \n" % (title, eval(title)))