# P1009 [NOIP1998 普及组] 阶乘之和 https://www.luogu.com.cn/problem/P1009

from typing import Dict

n = int(input())

factorial_dict = {}  # type: Dict[int, int]

s = 0

for i in range(1, n + 1):
    f = 1
    if factorial_dict.get(i - 1):
        f = factorial_dict[i - 1] * i
    factorial_dict[i] = f
    s += f

print(s)
