# P1596 [USACO10OCT]Lake Counting S https://www.luogu.com.cn/problem/P1596
# https://www.luogu.com.cn/record/71262438

import sys

sys.setrecursionlimit(10010)
N, M = map(int, input().split())
grid = [list(input().strip()) for _ in range(N)]
vis = [[0] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if grid[i][j] == '.':
            vis[i][j] = 1
dv = ((-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1))
result = 0


def dfs(x: int, y: int):
    for dx, dy in dv:
        nx = dx + x
        ny = dy + y
        if 0 <= nx < N and 0 <= ny < M and not vis[nx][ny]:
            vis[nx][ny] = 1
            dfs(nx, ny)


for i in range(N):
    for j in range(M):
        if not vis[i][j]:
            result += 1
            vis[i][j] = 1
            dfs(i, j)
print(result)
