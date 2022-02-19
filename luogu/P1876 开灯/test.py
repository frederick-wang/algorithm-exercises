# P1876 开灯 https://www.luogu.com.cn/problem/P1876

from typing import List

N = int(input())

nums: List[int] = []
i = 1
while (n := i * i) <= N:
    nums.append(n)
    i += 1
print(' '.join(map(str, nums)))
