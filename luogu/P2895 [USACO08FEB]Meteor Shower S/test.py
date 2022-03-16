# P2895 [USACO08FEB]Meteor Shower S https://www.luogu.com.cn/problem/P2895

from collections import deque
from typing import Deque, Tuple

M = int(input())
MAX_T = 1000000
ruined_grid = [[MAX_T] * 311 for _ in range(311)]
final_meteor_t = 0
for _ in range(M):
    x, y, t = map(int, input().split())
    if 0 <= y <= 310:
        if 0 <= x - 1 <= 310:
            ruined_grid[x - 1][y] = min(t, ruined_grid[x - 1][y])
        if 0 <= x <= 310:
            ruined_grid[x][y] = min(t, ruined_grid[x][y])
        if 0 <= x + 1 <= 310:
            ruined_grid[x + 1][y] = min(t, ruined_grid[x + 1][y])
    if 0 <= x <= 310:
        if 0 <= y - 1 <= 310:
            ruined_grid[x][y - 1] = min(t, ruined_grid[x][y - 1])
        if 0 <= y + 1 <= 310:
            ruined_grid[x][y + 1] = min(t, ruined_grid[x][y + 1])
    if t > final_meteor_t:
        final_meteor_t = t
grid = [[MAX_T] * 311 for _ in range(311)]
que: Deque[Tuple[int, int]] = deque()
dv = ((-1, 0), (1, 0), (0, -1), (0, 1))

que.append((0, 0))
grid[0][0] = 0

while len(que):
    x, y = que.popleft()
    if grid[x][y] > final_meteor_t:
        break
    for dx, dy in dv:
        nx = x + dx
        ny = y + dy
        nt = grid[x][y] + 1
        if 0 <= nx <= 310 and 0 <= ny <= 310 and nt < ruined_grid[nx][
                ny] and nt < grid[nx][ny]:
            grid[nx][ny] = nt
            que.append((nx, ny))
min_safe_t = MAX_T
for i in range(310):
    for j in range(310):
        if ruined_grid[i][j] == MAX_T and grid[i][j] < ruined_grid[i][j]:
            min_safe_t = min(min_safe_t, grid[i][j])
if min_safe_t == MAX_T:
    print(-1)
else:
    print(min_safe_t)
