# P1434 [SHOI2002]滑雪 https://www.luogu.com.cn/problem/P1434

import sys
from itertools import product

sys.setrecursionlimit(10005)
R, C = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(R)]
dv = ((0, 1), (0, -1), (1, 0), (-1, 0))
mem = [[0] * C for _ in range(R)]
vis = [[False] * C for _ in range(R)]


def dfs(x: int, y: int) -> int:
    vis[x][y] = True
    if not mem[x][y]:
        for dx, dy in dv:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < R and 0 <= ny < C and g[x][y] < g[nx][ny]:
                mem[x][y] = max(mem[x][y], dfs(nx, ny) + 1)
    return mem[x][y]


max_result = 0
for i, j in product(range(R), range(C)):
    if not vis[i][j]:
        mem = [[0] * C for _ in range(R)]
        max_result = max(max_result, dfs(i, j) + 1)
print(max_result)
