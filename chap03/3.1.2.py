list1 =[1, 2, 3, 4]
list2 = [1, 1.5, 'a', 'a', '문자열']
tuple1 =(1, 2)
tuple2 =(1, 1.5, 'b', 'b', '문자열' )
dict1={'name': '배종욱', 'email':'daum.net'}
set1, set2 = set(list2), set(tuple2)

list1[0] = 5 #0번 원소 값 변경
list2.insert(3,'b') #원소 삽입
# 튜플은 원소 변경 불가
dict1['email'] = 'naver.com' # 키 값으로 접근

print('list1', list1, type(list1))  # 객체 원소 및 자료형 출력
print('list2', list2, type(list2))

print('tuple1', tuple1, type(tuple1))

print('dict1', dict1, type(dict1))

print('set1', set1, type(set1))

print('set2', set2, type(set2))

print('intersection', set1 & set2)  # 교집합 구함
