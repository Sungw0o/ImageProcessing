import matplotlib.pyplot as plt
import numpy as np

x = np.arange(10)
y1 = np.arange(10)
y2 = np.arange(10)**2
y3 = np.random.choice(50, size=10)

plt.figure(figsize=(5,3))           				# 그림 객체 생성 - 그래프 크기(단위inch)
plt.plot(x, y1, 'b--', linewidth=2)					# 선 스타일 지정 – 파란색, 파선
plt.plot(x, y2, 'go-', linewidth=3)					# 녹색, 원 마크, 실선
plt.plot(x, y3, 'c+:', linewidth=5)					# 청록색, +마크, 점선


plt.title("Line examples")    						# 그래프 제목
plt.axis([0,10, 0,80])								# 축 범위 설정 X축은 (0 ~ 10) Y 축은 (0 ~80)

# 자동으로 레아아웃 조정하여 간격을 최적화
plt.tight_layout()
plt.savefig(fname="sample.png", dpi=300)			# 그림 저장 해상도 300dpi
plt.show()				 							# 윈도우 표시