# P3916 图的遍历 https://www.luogu.com.cn/problem/P3916

import sys

sys.setrecursionlimit(100005)

N, M = map(int, sys.stdin.readline().split())
p = [[] for _ in range(N + 1)]
ans = [0] * N
for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    p[v].append(u)


def dfs(x: int, target: int):
    if not ans[x - 1]:
        ans[x - 1] = target
        for u in p[x]:
            dfs(u, target)


for target in range(N, 0, -1):
    dfs(target, target)

sys.stdout.write(' '.join(map(str, ans)))
