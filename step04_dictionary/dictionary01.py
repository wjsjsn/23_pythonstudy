# dictionary : key와 값의 쌍, 인덱싱 불가
#              key를 통해 값을 검색
# 형식 : {key1 : value1, key2 : value2 , ...}
# 특징
# 1. type에서 dict 클래스로 구현
# 2. dictionary의 key는 변경할 수 x, 값은 변경 가능

dic = {101 : "둘리", 201 : '도우너', 301 : '마이콜', 401 : '또치'}
print(type(dic))

print(dic[101]) # key를 통해 값을 검색

# key를 이용해서 값을 변경(기존 값을 덮어쓰기함)
dic[101] = '태권브이'
print(dic[101])

