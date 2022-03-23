# P1996 约瑟夫问题 https://www.luogu.com.cn/problem/P1996

from collections import deque

N, M = map(int, input().split())
que = deque(range(1, N + 1))
num = 1
while len(que):
    item = que.popleft()
    if num == M:
        print(item, end=' ')
        num = 1
    else:
        que.append(item)
        num += 1
