import matplotlib.pyplot as plt

# fig = plt.figure(figsize=(5, 5)) # 새 figure을 생성하며 크기 지정
# plt.show()

# fig = plt.figure()
# ax = fig.add_subplot(1, 1, 1)
# # 창을 가로 1칸, 세로 1칸으로 분할하고 그 중 첫 번째 칸에 ax라는 axes 생성
# plt.show()

fig = plt.figure()
# 가로 2칸, 세로 1칸, 첫번째 칸에 ax1, 두번째 칸에 ax2 생성
ax1 = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(1, 2, 2)
plt.show()