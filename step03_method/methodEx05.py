num = [10, 20, 30, 40, 50]
print(type(num)) # 해당 변수의 타입

num2 = (10, 20, 30, 40, 50)
print(type(num2))

for i in num:
    print(i) # 자동으로 줄바꿈

print('*' * 30)

for i in num:
    print(i, end=' ') # 자동으로 줄바꿈 x => 띄어쓰기

print()
print('*' * 30)

# 인덱스값 이용
for i in range(0,  num.__len__()):
    print(num[i], end=' ')

print()
print('*' * 30)

# 역순으로 출력
for i in range(num.__len__()-1, -1, -1):
    print(num[i], end=' ')

print()
print('*' * 30)
