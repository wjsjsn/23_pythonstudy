# 난수 함수
# from random import random
from random import *
# import random

# 0.0 이상 1.0 미만의 임의 실수
# print(random)
print(random())

# 1.0 이상 3.0 미만
print(uniform(1.0, 3.0))

# 1 이상 10 이하
print(randint(1, 10))

# 1부터 100 미만까지의 3의 배수 중 하나
print(randrange(3, 100, 3))

# 리스트 안에 존재하는 값 중 하나
print(choice([1, 54, 9, 32, 75, 11]))