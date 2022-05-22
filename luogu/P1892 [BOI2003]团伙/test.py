# P1892 [BOI2003]团伙 https://www.luogu.com.cn/problem/P1892

from sys import stdin
from typing import Dict, Set

N = int(stdin.readline())
M = int(stdin.readline())

fa = list(range(N + 1))


def find(x: int) -> int:
    if fa[x] != x:
        fa[x] = find(fa[x])
    return fa[x]


def unite(x: int, y: int):
    fa[find(x)] = find(y)


friend: Dict[int, Set[int]] = {}
enemy: Dict[int, Set[int]] = {}
for _ in range(M):
    raw_input = stdin.readline().split()
    p = int(raw_input[1])
    q = int(raw_input[2])
    if raw_input[0] == 'F':
        if p in friend:
            friend[p].add(q)
        else:
            friend[p] = {q}
        if q in friend:
            friend[q].add(p)
        else:
            friend[q] = {p}
        unite(p, q)
    else:
        if p in enemy:
            enemy[p].add(q)
        else:
            enemy[p] = {q}
        if q in enemy:
            enemy[q].add(p)
        else:
            enemy[q] = {p}

vis = [False] * (N + 1)

for i in range(1, N + 1):
    if i in enemy and not vis[i]:
        for j in enemy[i]:
            if j in enemy:
                for k in enemy[j]:
                    if i != k:
                        vis[k] = True
                        unite(i, k)

print(sum(x == find(x) for x in range(1, N + 1)))
