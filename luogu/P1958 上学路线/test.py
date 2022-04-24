# P1958 上学路线 https://www.luogu.com.cn/problem/P1958

A, B = map(int, input().split())
g = [[0] * (B + 1) for _ in range(A + 1)]
N = int(input())
o = [[0] * (B + 1) for _ in range(A + 1)]
for _ in range(N):
    X_i, Y_i = map(int, input().split())
    o[X_i][Y_i] = 1
mem = [[0] * (B + 1) for _ in range(A + 1)]
dv = ((1, 0), (0, 1))


def dfs(x: int, y: int) -> int:
    if x == A and y == B:
        return 1
    if not mem[x][y]:
        for dx, dy in dv:
            nx = x + dx
            ny = y + dy
            if 1 <= nx <= A and 1 <= ny <= B and not o[nx][ny] and not g[nx][ny]:
                g[nx][ny] = 1
                mem[x][y] += dfs(nx, ny)
                g[nx][ny] = 0
    return mem[x][y]


print(dfs(1, 1))
