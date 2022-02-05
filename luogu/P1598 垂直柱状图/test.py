# P1598 垂直柱状图 https://www.luogu.com.cn/problem/P1598

from collections import Counter
from curses.ascii import isupper

stat = Counter('')
for _ in range(4):
    stat.update(filter(isupper, input()))

max_num = max(stat.values())

for i in range(max_num):
    print(' '.join([
        '*' if stat[chr(j)] + i >= max_num else ' ' for j in range(65, 65 + 26)
    ]).rstrip())
print(' '.join(map(chr, range(65, 65 + 26))))
