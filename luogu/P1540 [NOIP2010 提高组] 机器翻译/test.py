# P1540 [NOIP2010 提高组] 机器翻译 https://www.luogu.com.cn/problem/P1540

from collections import deque
from typing import Deque

M, N = map(int, input().split())
mem: Deque[int] = deque()
query_times = 0
for word in map(int, input().split()):
    if word not in mem:
        query_times += 1
        if len(mem) >= M:
            mem.popleft()
        mem.append(word)
print(query_times)
