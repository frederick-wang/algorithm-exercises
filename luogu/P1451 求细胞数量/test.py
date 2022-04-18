# P1451 求细胞数量 https://www.luogu.com.cn/problem/P1451

import itertools

N, M = map(int, input().split())
matrix = [list(input().strip()) for _ in range(N)]
vis = [[False] * M for _ in range(N)]
dv = ((1, 0), (-1, 0), (0, 1), (0, -1))
cnt = 0


def dfs(x: int, y: int):
    vis[x][y] = True
    for dx, dy in dv:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < N and 0 <= ny < M and matrix[nx][ny] != '0' and not vis[
                nx][ny]:
            dfs(nx, ny)


for i, j in itertools.product(range(N), range(M)):
    if matrix[i][j] != '0' and not vis[i][j]:
        cnt += 1
        dfs(i, j)

print(cnt)
