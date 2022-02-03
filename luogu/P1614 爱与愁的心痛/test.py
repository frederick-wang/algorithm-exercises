# P1614 爱与愁的心痛 https://www.luogu.com.cn/problem/P1614

from typing import List

n, m = map(int, input().split())

min_sum = 300000 if n else 0

last_nums = []  # type: List[int]

for i in range(n):
    a = int(input())
    if m - 1 < 0:
        min_sum = 0
        break
    if m - 1 == 0:
        if a < min_sum:
            min_sum = a
        continue
    if i < m - 1:
        last_nums.append(a)
        continue
    s = a + sum(last_nums)
    if s < min_sum:
        min_sum = s
    last_nums.pop(0)
    last_nums.append(a)

print(min_sum)
