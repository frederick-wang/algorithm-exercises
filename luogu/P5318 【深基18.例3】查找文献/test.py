# P5318 【深基18.例3】查找文献 https://www.luogu.com.cn/problem/P5318
# 用 PyPy3 提交

import sys
from collections import deque
from typing import Deque, List

sys.setrecursionlimit(100005)

N, M = map(int, sys.stdin.readline().split())
p: List[List[int]] = [[] for _ in range(N + 1)]
vis = [False] * (N + 1)
for _ in range(M):
    x, y = map(int, sys.stdin.readline().split())
    p[x].append(y)
for to_list in p:
    to_list.sort()

out_dfs: List[int] = []


def dfs(x: int) -> None:
    vis[x] = True
    out_dfs.append(x)
    for y in p[x]:
        if not vis[y]:
            dfs(y)


dfs(1)
print(' '.join(map(str, out_dfs)))

out_bfs: List[int] = []

vis[:] = [False] * (N + 1)
que: Deque[int] = deque()
que.append(1)
vis[1] = True
while len(que):
    x = que.popleft()
    out_bfs.append(x)
    for y in p[x]:
        if not vis[y]:
            que.append(y)
            vis[y] = True
print(' '.join(map(str, out_bfs)))
