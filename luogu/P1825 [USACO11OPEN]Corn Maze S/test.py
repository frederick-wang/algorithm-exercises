# P1825 [USACO11OPEN]Corn Maze S https://www.luogu.com.cn/problem/P1825

from collections import deque
from typing import Deque, Dict, Tuple

# 用 X 指 行，用 Y 指 列
Pair = Tuple[int, int]  # (行, 列)
INF = int(999)
dx = (0, 0, -1, 1)
dy = (-1, 1, 0, 0)

device_idx: Dict[str, Dict[Pair, int]] = {}
device: Dict[str, Dict[int, Pair]] = {}
device_times: Dict[Pair, bool] = {}

N, M = map(int, input().split())
m = [[''] * M for _ in range(N)]
d = [[INF] * M for _ in range(N)]
sx, sy = -1, -1
fx, fy = -1, -1

# 初始化数据
device_i: Dict[str, int] = {chr(i): 0 for i in range(65, 91)}
for i in range(N):
    row = input().strip()
    for j in range(M):
        c = row[j]
        m[i][j] = c
        if c == '@':
            sx, sy = i, j
        if c == '=':
            fx, fy = i, j
        if c.isalpha():
            p = (i, j)
            c_i = device_i[c]
            if c in device:
                device[c][c_i] = p
                device_idx[c][p] = c_i
            else:
                device[c] = {c_i: p}
                device_idx[c] = {p: c_i}
                device_i[c] += 1
device_enabled = {c: len(device[c]) > 1 for c in device}


def bfs() -> int:
    que: Deque[Pair] = deque([(sx, sy)])
    d[sx][sy] = 0

    while len(que):
        p = que.popleft()
        px, py = p
        if p == (fx, fy):
            return d[fx][fy]
        for i in range(4):
            nx, ny = px + dx[i], py + dy[i]
            np = (nx, ny)
            c = m[nx][ny]
            if 0 <= nx < N and 0 <= ny < M and c != '#':
                if c.isalpha() and device_enabled[c]:
                    if np not in device_times:
                        nnx, nny = device[c][1 - device_idx[c][np]]
                        que.append((nnx, nny))
                        d[nnx][nny] = d[px][py] + 1
                        device_times[np] = True
                else:
                    if INF == d[nx][ny]:
                        que.append(np)
                        d[nx][ny] = d[px][py] + 1
    return d[fx][fy]


print(bfs())
