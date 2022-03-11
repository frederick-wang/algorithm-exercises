# P1162 填涂颜色 https://www.luogu.com.cn/problem/P1162

N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]
mask = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if grid[i][j] == 1:
            mask[i][j] = 1
dv = ((-1, 0), (1, 0), (0, -1), (0, 1))


def dfs(x: int, y: int):
    for dx, dy in dv:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < N and 0 <= ny < N and not mask[nx][ny]:
            mask[nx][ny] = 1
            dfs(nx, ny)


for i in range(N):
    if i == 0 or i == N - 1:
        # 避免 mypy 报错
        rangeJ = tuple(range(N))
    else:
        rangeJ = (0, N - 1)
    for j in rangeJ:
        if not mask[i][j]:
            mask[i][j] = 1
            dfs(i, j)

for i in range(N):
    print(' '.join(
        map(lambda x: str(x[1]) if mask[i][x[0]] else '2', enumerate(grid[i]))))
