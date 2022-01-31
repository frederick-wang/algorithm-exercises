# P1422 小玉家的电费 https://www.luogu.com.cn/problem/P1422

x = int(input())

cost = 0.0

if x <= 150:
    cost = x * 0.4463
elif x <= 400:
    cost = 150 * 0.4463 + (x - 150) * 0.4663
else:
    cost = 150 * 0.4463 + 250 * 0.4663 + (x - 400) * 0.5663

print('%.1f' % cost)
