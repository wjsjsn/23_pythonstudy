import sys

s1 = int(input("수를 입력하세요 : "))

# 파이썬에서 타입 확인 : type()
# print(type(s1))


'''
# if문
if s1 == 0 :
    print("0은 나눗셈을 이용할 수 없습니다.")
    sys.exit(0)

print('3/', s1, '=', 3/s1)

# if ~ else문
if s1 == 0 :
    print("0은 나눌 수 없습니다.")
else :
    print('3/', s1, '=', 3/s1)
    
'''

# 다중 if문
if s1 >= 90 : 
    print("A학점")
elif s1 >= 80 :
    print("B학점")
elif s1 >= 70 :
    print("C학점")
else :
    print("F학점")