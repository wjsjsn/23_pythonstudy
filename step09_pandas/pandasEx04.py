import pandas as pd
import pandasEx02 as ex02

# in : 주로 검색 용도로 사용
print('서울' in ex02.city) # True
print('수원' in ex02.city) # False
print('-' * 50)

# 인덱스만
for i in ex02.city.index:
    print(i, end='')
print()
print('-' * 50)

# 값만
for i in ex02.city.values:
    print(i, end='  ')
print()
print('-' * 50)

# 둘 다
for k, v in ex02.city.items():
    print('%s = %d' %(k, v))
print('-' * 50)

print('---------- dictionary 객체에서 시리즈 생성 ----------')
city2 = pd.Series({'서울' : 10022181, '대전' : 1518775, '대구' : 2487829, '부산' : 3531777})
print(city2)
print('-' * 50)

# 순서를 변경하고자 하면 index를 리스트로 지정하면 됨
print('---- 딕셔너리 객체에서 시리즈 생성 (순서변경) ----')
city3 = pd.Series({'서울' : 10022181, '대전':1518775, '대구':2487829, '부산':3531777, '인천':2925815},
                  index=['서울','부산','대구','대전','인천'])
print(city3)

print('--- 인덱스 기반 연산 ---')
res = ex02.city - city2
print(res)
print(type(res))

print('--- 인덱스 기반 연산2 ---')
res2 = ex02.city.values - city2.values
print(res2)
print(type(res2))

print('--- 인덱스 기반 연산(인천없네) ---')
res3 = ex02.city - city3
print(res3)
