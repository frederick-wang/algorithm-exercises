# P1525 [NOIP2010 提高组] 关押罪犯 https://www.luogu.com.cn/problem/P1525

from sys import stdin, setrecursionlimit
from typing import List, Tuple

setrecursionlimit(100005)

N, M = map(int, stdin.readline().split())
fa = list(range(N + 1))
enemy = [0] * (N + 1)


def find(x: int) -> int:
    if fa[x] != x:
        fa[x] = find(fa[x])
    return fa[x]


r: List[Tuple[int, int, int]] = [
    tuple(map(int,
              stdin.readline().split())) for _ in range(M)
]
r.sort(reverse=True, key=lambda x: x[2])

for x, y, val in r:
    fx = find(x)
    fy = find(y)
    if fx == fy:
        print(val)
        exit()
    if enemy[x]:
        fa[find(enemy[x])] = fy
    else:
        enemy[x] = y
    if enemy[y]:
        fa[find(enemy[y])] = fx
    else:
        enemy[y] = x
print(0)
