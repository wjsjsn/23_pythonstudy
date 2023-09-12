# 파이썬은 switch문 x
# dictionary를 이용해 switch와 같은 기능 사용

def switch(x) :
    return{
        'one' : 1,
        'two' : 2,
        'three' : 3
    }.get(x, "알 수 없음") # switch-default

print(switch("two"))
print(switch(100))