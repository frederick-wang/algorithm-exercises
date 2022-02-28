# P1002 [NOIP2002 普及组] 过河卒 https://www.luogu.com.cn/problem/P1002

B_N, B_M, H_N, H_M = map(int, input().split())
d = ((1, 0), (0, 1))
d_horse = ((0, 0), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2),
           (-2, -1))

grid = [[True] * (B_M + 1) for _ in range(B_N + 1)]
for di, dj in d_horse:
    if 0 <= (ni := H_N + di) <= B_N and 0 <= (nj := H_M + dj) <= B_M:
        grid[ni][nj] = False
record = [[-1] * (B_M + 1) for _ in range(B_N + 1)]


def dfs(i: int, j: int) -> int:
    if i == B_N and j == B_M:
        return 1
    if record[i][j] == -1:
        record[i][j] = 0
        for di, dj in d:
            if 0 <= (ni := i + di) <= B_N and 0 <= (nj := j +
                                                    dj) <= B_M and grid[ni][nj]:
                record[i][j] += dfs(ni, nj)
    return record[i][j]


print(dfs(0, 0))
