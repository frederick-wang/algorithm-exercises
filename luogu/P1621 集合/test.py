# P1621 集合 https://www.luogu.com.cn/problem/P1621

from math import ceil, sqrt
from sys import stdin, setrecursionlimit

setrecursionlimit(100005)

A, B, P = map(int, stdin.readline().split())
fa = list(range(B + 1))


def find(x: int) -> int:
    if fa[x] != x:
        fa[x] = find(fa[x])
    return fa[x]


def unite(x: int, y: int):
    fa[find(x)] = find(y)


prime = [True] * (B + 1)
prime[0] = False
prime[1] = False
for i in range(2, int(sqrt(B)) + 1):
    if prime[i]:
        for j in range(i * i, B + 1, i):
            prime[j] = False
for i in range(P, B + 1):
    if prime[i]:
        for factor in range(ceil(A / i), B // i):
            unite(i * factor, i * (factor + 1))
print(sum(x == find(x) for x in range(A, B + 1)))
