# P1551 亲戚 https://www.luogu.com.cn/problem/P1551

from typing import Dict

N, M, P = map(int, input().split())

d: Dict[int, int] = {}

idx = 0
for _ in range(M):
    a, b = map(int, input().split())
    if a not in d and b not in d:
        d[a] = idx
        d[b] = idx
        idx += 1
    elif a in d and b not in d:
        i = d[a]
        d[b] = i
    elif a not in d and b in d:
        i = d[b]
        d[a] = i
    else:
        i_a = d[a]
        i_b = d[b]
        for num, i in d.items():
            if i == i_b:
                d[num] = i_a

for _ in range(P):
    a, b = map(int, input().split())
    # NOTE: 自己和自己也算亲戚
    print('Yes' if a == b or d.get(a, -1) == d.get(b, -2) else 'No')
