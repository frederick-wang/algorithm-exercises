# P1147 连续自然数和 https://www.luogu.com.cn/problem/P1147

from typing import Dict
from array import array

M = int(input())
s = array('L', [0, 1])
d: Dict[int, int] = {}
for i in range(2, M + 1):
    s_i = s[i - 1] + i
    if s_i - s[i - 2] > M:
        break
    s.append(s_i)
    d[s_i] = i
for i in range(1, len(s)):
    if i >= 2 and s[i] - s[i - 2] > M:
        break
    if (right := M + s[i]) in d:
        print(i + 1, d[right])
