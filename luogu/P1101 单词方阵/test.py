# P1101 单词方阵 https://www.luogu.com.cn/problem/P1101

from typing import List, Tuple

word = 'yizhong'
WORD_LEN = len(word)
N = int(input())
grid = [[''] * N for _ in range(N)]
y_points: List[Tuple[int, int]] = []
for i in range(N):
    for j, c in enumerate(input().strip()):
        if c in word:
            grid[i][j] = c
            if c == 'y':
                y_points.append((i, j))
        else:
            grid[i][j] = '*'
dv = ((-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, -1), (-1, 1), (1, 1))
flag = [[0] * N for _ in range(N)]


def dfs(x: int, y: int, i: int, d: int) -> bool:
    if i == WORD_LEN - 1:
        return True
    dx, dy = dv[d]
    nx = x + dx
    ny = y + dy
    if 0 <= nx < N and 0 <= ny < N and grid[nx][ny] != '*':
        if grid[nx][ny] == word[i + 1]:
            if dfs(nx, ny, i + 1, d):
                flag[nx][ny] = 1
                return True
    return False


for x, y in y_points:
    for d in range(len(dv)):
        if dfs(x, y, 0, d):
            flag[x][y] = True

for i in range(N):
    print(''.join(
        map(lambda x: x[1] if flag[i][x[0]] else '*', enumerate(grid[i]))))
