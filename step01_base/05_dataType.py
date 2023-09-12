'''
    딕셔너리 : key와 values로 이루어짐
             key는 불변하는 값만 넣을 수 있음
'''
import bz2

d1 = {1 : "Hello"}
print(d1) # {1: 'Hello'}
print(d1[1]) # Hello

# 추가
d1[2] = "홍길동"
d1[5] = "고길동"
print(d1) # {1: 'Hello', 2: '홍길동', 5: '고길동'}
d1['둘리'] = 24
d1['마이콜'] = 38
print(d1) # {1: 'Hello', 2: '홍길동', 5: '고길동', '둘리': 24, '마이콜': 38}

# key는 중복 x(같은 key에 다른 값이 들어오면 덮어씀)
d1[1] = 'hi'
print(d1)

d1['num'] = [1, 2, 3]
print(d1)

# key를 이용해서 삭제 가능
del d1['num']
print(d1)

# key에 리스트 사용 x, 튜플은 가능
d2 = {"name":"홍길동", "hp":"010-7979-7979", "age":24}

# keyList 만드는 함수 : keys()
res = d2.keys()
print(res) # dict_keys(['name', 'hp', 'age'])

for k in d2.keys():
    print(k) # name hp age 하나씩 나옴

# key를 리스트로 변환 : list(변수.keys())
res2 = list(d2.keys())
print(res2) # ['name', 'hp', 'age']

# values를 리스트로 변환 : list(변수.values())
res3 = list(d2.values())
print(res3) # ['홍길동', '010-7979-7979', 24]

res3 = d2.values()
print(res3) # dict_values(['홍길동', '010-7979-7979', 24])

# key, values 한 쌍 얻기 : items()
# 리턴값은 dict_items 객체이고 튜플로 구성
res4 = d2.items()
print(res4) # dict_items([('name', '홍길동'), ('hp', '010-7979-7979'), ('age', 24)])

# key를 이용해서 값 얻어오기 : get()
k1 = d2.get('age')
print(k1) # 24

# 이렇게 해도 됨
k2 = d2['age']
print(k2) # 24

# 없는 key 넣기 => None 나옴
k3 = d2.get('gender')
print(k3) # None

# 이건 오류 남
# k4 = d2['gender']
# print(k4)

# 딕셔너리에서 해당 key가 존재하는지 알아보기
# 파이썬에서는 True, False는 무조건 첫 글자가 대문자여야함 아니면 오류
res5 = 'age' in d2
print(res5) # True

res6 = 'gender' in d2
print(res6) # False

# 전부 삭제 : clear()
# d2.clear()
# print(d2) # {}

# 하나만 삭제 : del, pop()
del d2['age']
print(d2) # {'name': '홍길동', 'hp': '010-7979-7979'}

d2.pop('name')
print(d2) # {'hp': '010-7979-7979'}

# 항목의 개수 구하기 : len()
res7 = len(d2)
print(res7) # 1