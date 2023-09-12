# https://matplotlib.org/ 사이트 참조

import matplotlib.pyplot as plt

names = ["Python", "Java", "Spring", "Flask"] # x축의 값
score = [155, 301, 125, 98] # y축의 값

plt.plot(names, score)
plt.show()