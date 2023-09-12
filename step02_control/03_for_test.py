# 1-10까지의 합, 홀수의 합, 짝수의 합 구하기

hap = 0
odd = 0
even = 0

# range(11) : 0 - 10
for i in range(11):
    hap += i
    if(i % 2) == 0 :
        even += i
    else :
        odd += i
print('0-10까지의 합 : ', hap)
print('짝수의 합 : ', even)
print('홀수의 합 : ', odd)

print("범위(range) : ", sum(range(11)))
