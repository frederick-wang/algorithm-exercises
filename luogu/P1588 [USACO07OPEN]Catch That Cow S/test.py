# P1588 [USACO07OPEN]Catch That Cow S https://www.luogu.com.cn/problem/P1588

from collections import deque
from typing import Deque

INF = 1000000000
LEN = 200000
T = int(input())

for _ in range(T):
    X, Y = map(int, input().split())
    min_n = abs(X - Y)
    road = [INF] * LEN
    que: Deque[int] = deque()
    que.append(X)
    road[X] = 0
    while len(que):
        x = que.popleft()
        n = road[x]
        if x == Y:
            min_n = min(min_n, n)
        nn = n + 1
        if nn >= min_n:
            continue
        nx = x - 1
        if 0 <= nx < LEN and nn < road[nx]:
            road[nx] = nn
            que.append(nx)
        nx = x + 1
        if 0 <= nx < LEN and nn < road[nx]:
            road[nx] = nn
            que.append(nx)
        nx = 2 * x
        if 0 <= nx < LEN and nn < road[nx]:
            road[nx] = nn
            que.append(nx)
    print(min_n)
