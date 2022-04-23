# P1644 跳马问题 https://www.luogu.com.cn/problem/P1644

N, M = map(int, input().split())
dv = ((2, 1), (1, 2), (-1, 2), (-2, 1))
board = [[0] * (M + 1) for _ in range(N + 1)]
mem = [[-1] * (M + 1) for _ in range(N + 1)]


def dfs(x: int, y: int) -> int:
    if x == N and y == M:
        return 1
    if mem[x][y] == -1:
        mem[x][y] = 0
        for dx, dy in dv:
            nx = x + dx
            ny = y + dy
            if 0 <= nx <= N and 0 <= ny <= M and not board[nx][ny]:
                board[nx][ny] = 1
                mem[x][y] += dfs(nx, ny)
                board[nx][ny] = 0
    return mem[x][y]


print(dfs(0, 0))
