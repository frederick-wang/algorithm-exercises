# P1141 01迷宫 https://www.luogu.com.cn/problem/P1141

from collections import deque
from typing import Deque, Tuple

INF = int(1e9)
N, M = map(int, input().split())
grid = [input().strip() for _ in range(N)]
dv = ((1, 0), (-1, 0), (0, 1), (0, -1))
que: Deque[Tuple[int, int]] = deque()
to_update: Deque[Tuple[int, int]] = deque()
vis = [[0] * N for _ in range(N)]


def bfs(start_x: int, start_y: int) -> int:
    if vis[start_x][start_y]:
        return vis[start_x][start_y]
    que.append((start_x, start_y))
    to_update.append((start_x, start_y))
    vis[start_x][start_y] = 1
    ans = 1
    while len(que):
        x, y = que.popleft()
        for dx, dy in dv:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < N and not vis[nx][ny] and grid[nx][
                    ny] == ('1' if grid[x][y] == '0' else '0'):
                vis[nx][ny] = 1
                ans += 1
                que.append((nx, ny))
                to_update.append((nx, ny))
    while len(to_update):
        x, y = to_update.popleft()
        vis[x][y] = ans
    return ans


for _ in range(M):
    i, j = map(int, input().split())
    print(bfs(i - 1, j - 1))
