# P1104 生日 https://www.luogu.com.cn/problem/P1104

from typing import List, Tuple

N = int(input())
l: List[Tuple[int, int, int, int, str]] = []

for i in range(N):
    raw = input().split()
    s = raw[0]
    y, m, d = map(int, raw[1:])
    l.append((y, m, d, -i, s))
l.sort()
for v in l:
    print(v[4])
