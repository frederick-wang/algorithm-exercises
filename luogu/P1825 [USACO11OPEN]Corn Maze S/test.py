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
            if c in device:
                device[c][device_i[c]] = (i, j)
                device_idx[c][(i, j)] = device_i[c]
            else:
                device[c] = {device_i[c]: (i, j)}
                device_idx[c] = {(i, j): device_i[c]}
                device_i[c] += 1


def bfs() -> int:
    que: Deque[Pair] = deque([(sx, sy)])
    d[sx][sy] = 0

    while len(que):
        # print(' ' * 7, end='')
        # for i in range(M):
        #     print('%06d' % i, end=' ')
        # print()
        # for r_i, row in enumerate(d):
        #     for c_i, col in enumerate(row):
        #         if c_i == 0:
        #             print('%06d' % r_i, end=' ')
        #         print('%03d(%s)' % (col, m[r_i][c_i]), end=' ')
        #     print()
        # print()
        p = que.popleft()
        # print('-:', p, '%03d(%s)' % (d[p[0]][p[1]], m[p[0]][p[1]]))
        px, py = p
        if p == (fx, fy):
            return d[fx][fy]
        for i in range(4):
            nx, ny = px + dx[i], py + dy[i]
            c = m[nx][ny]
            new_d = d[px][py] + 1
            if 0 <= nx < N and 0 <= ny < M and c != '#':
                if c.isalpha() and len(device[c]) > 1:
                    if (nx, ny) not in device_times:
                        # print(c, device[c], len(device[c]))
                        n2x, n2y = device[c][1 - device_idx[c][(nx, ny)]]
                        que.append((n2x, n2y))
                        d[n2x][n2y] = new_d
                        device_times[(nx, ny)] = True
                        # print('+:', (n2x, n2y),
                        #       '%03d(%s)' % (d[n2x][n2y], m[n2x][n2y]))
                        # print('+:', (nx, ny),
                        #       '%03d(%s)' % (d[nx][ny], m[nx][ny]))
                else:
                    if new_d < d[nx][ny]:
                        que.append((nx, ny))
                        d[nx][ny] = new_d
                        # print('+:', (nx, ny),
                        #       '%03d(%s)' % (d[nx][ny], m[nx][ny]))
    return d[fx][fy]


print(bfs())
