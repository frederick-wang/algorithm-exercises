# P1605 迷宫 https://www.luogu.com.cn/problem/P1605

N, M, T = map(int, input().split())
grid = [[0] * (M + 1) for _ in range(N + 1)]
SX, SY, FX, FY = map(int, input().split())
for _ in range(T):
    tx, ty = map(int, input().split())
    grid[tx][ty] = 1
result = 0
dv = ((-1, 0), (1, 0), (0, -1), (0, 1))


def dfs(x: int, y: int):
    global result
    if x == FX and y == FY:
        result += 1
        return
    for dx, dy in dv:
        nx = x + dx
        ny = y + dy
        if 1 <= nx <= N and 1 <= ny <= M and grid[nx][ny] == 0:
            grid[nx][ny] = 1
            dfs(nx, ny)
            grid[nx][ny] = 0


grid[SX][SY] = 1
dfs(SX, SY)
print(result)
