print("첫 번째 수를 입력하세요 : ")
s1 = input()

print("두 번째 수를 입력하세요 : ")
s2 = input()

result = int(s1) + int(s2)
print("{0} + {1} = {2}".format(s1, s2, result)) # 10 + 5 = 15
print("{1} + {0} = {2}".format(s1, s2, result)) # 5 + 10 = 15

