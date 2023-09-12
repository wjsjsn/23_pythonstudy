dict_emp = {'name' : '뽀로로', 'phone' : '010-1234-3241', 'addr' : '강남구'}

# keys : 키 리스트 만들기
key = dict_emp.keys()
print(key)
print(type(key))

# keys를 활용한 출력
for i in dict_emp.keys():
    print(i)

# keys를 활용한 리스트 만들기
key2 = list(dict_emp.keys())
print(key2)
print(type(key2))

# values()를 활용
value = dict_emp.values()
print(value)
print(type(value))

for i in dict_emp.values():
    print(i)

# key를 이용한 value값 얻기
print('get() 이용 : ', dict_emp.get('name'))
print('[key값] 이용 : ', dict_emp['phone'])

# 해당 key가 dictionary에 있는지 조사(in)
print('name' in dict_emp) # key가 있으면 True
print('age' in dict_emp) # key가 없으면 False

# clear() : key, value 모두 지우기
dict_emp.clear()
print(dict_emp)

mydict = {'홍길동' : 20, '일지매' : 25, '임꺽정' : 31, '장길산' : 36}
for i in mydict:
    print(i, end=' ')
    print(mydict[i], end='')
    print()

print('*' * 30)

# 나이가 30 이상
for i in mydict:
    if mydict[i] >= 30:
        print(i, mydict[i])

print('*' * 30)

for name, age in mydict.items():
    if age == 31:
        print(name)

print('*' * 30)

# dictionary comprehension
[print(name) for name, age in mydict.items() if age == 31]

print('*' * 30)

[print(name) for name, age in mydict.items() if age != 31]

print('*' * 30)
