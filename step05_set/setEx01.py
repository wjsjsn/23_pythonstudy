# 컬렉션, 자료구조 => list[], tuple(), dictionary{키:값}, set{}
# Set : 집합, 중복 허용 x, 순서 유지 x

myset = {1, 2, 3}
print(type(myset))

# 추가 : add
myset.add(4.0)
myset.add("one")
print(myset)

print('*' * 30)

# 존재 유무
if myset.__contains__(3):
    print('존재함')
else:
    print('존재 안 함')

print('*' * 30)

# set 자료형에 저장된 값을 인덱싱으로 접근하려면 list나 tuple로 만들어야함
mylist = list(myset)
print(type(mylist))
print(mylist[0])

print('*' * 30)

mytuple = tuple(myset)
print(type(mytuple))
print(mytuple[2])

print('*' * 30)

# 교집합, 합집합, 차집합을 구할 때 유용
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])
print(type(s1), type(s2))

# 교집합 : &
print('교집합 : ', s1 & s2)
print('교집합 : ', s1.intersection(s2))
print('교집합 : ', s2.intersection(s1))

print('*' * 30)

# 합집합 : |
print('합집합 : ', s1|s2)
print('합집합 : ', s1.union(s2))
print('합집합 : ', s2.union(s1))

print('*' * 30)

# 차집합 : -
print('차집합 : ', s1 - s2)
print('차집합 : ', s1.difference(s2))
print('차집합 : ', s2 - s1)
print('차집합 : ', s2.difference(s1))

print('*' * 30)
