import numpy as np

list1, list2 = [1, 2, 3] , [4, 5.0, 6]
a, b = np.array(list1), np.array(list2) #리스트로 ndarry 객체 생성

c = a + b
d = a - b
e = a * b
f = a / b
g = a * 2 # 스칼라 곱
h = b + 2 # 스칼라 합

print('a 자료형', type(a), type(a[0]))
print('b 자료형', type(b), type(b[0]))
print('c 자료형', type(c), type(c[0]))
print('g 자료형', type(g), type(g[0]))
print(c, d, e)
print(f, g, h)