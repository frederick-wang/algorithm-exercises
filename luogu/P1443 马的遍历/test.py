# P1443 马的遍历 https://www.luogu.com.cn/problem/P1443
# https://www.luogu.com.cn/record/71461768

from collections import deque
from typing import Deque, Tuple

N, M, SX, SY = map(int, input().split())
grid = [[-1] * (M + 1) for _ in range(N + 1)]
dv = ((-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2))
que: Deque[Tuple[int, int]] = deque()
que.append((SX, SY))
grid[SX][SY] = 0

while len(que):
    x, y = que.popleft()
    for dx, dy in dv:
        nx = x + dx
        ny = y + dy
        d = grid[x][y] + 1
        if 1 <= nx <= N and 1 <= ny <= M and grid[nx][ny] == -1:
            grid[nx][ny] = d
            que.append((nx, ny))

templ = '%-5d' * M
for row in grid[1:]:
    print(templ % tuple(row[1:]))
