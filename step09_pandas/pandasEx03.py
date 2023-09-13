import pandas as pd
import pandasEx02 as ex02

# 한 번에 value값 계산 가능
div = ex02.city / 1000000
print(div)
print('-' * 50)

# 시리즈 인덱싱[0부터]
print(ex02.city[1])
print(ex02.city['대전'])

# 배열 인덱싱(순서 변경 가능)
print(ex02.city[[1, 3, 0]])
print('-' * 50)

print(ex02.city[['대전', '서울', '부산']])
print('-' * 50)

# 슬라이싱
print(ex02.city[1:3]) # 3은 포함 x
print('-' * 50)

a = pd.Series(range(3), index=['가', '1', 'A'])
print(a)
print('-' * 50)

print(a['A']) # 2
print('-' * 50)

print(a.A) # 2
print('-' * 50)

print(a['1']) # 1
print('-' * 50)

print(a.가) # 0
print('-' * 50)

b = pd.Series(range(10, 19)) # 인덱스 수랑 range 수랑 안 맞으면 오류남
print(b)
print('-' * 50)
