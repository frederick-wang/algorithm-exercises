# P1969 [NOIP2013 提高组] 积木大赛 https://www.luogu.com.cn/problem/P1969

import sys
import numpy as np

sys.setrecursionlimit(1000010)
N = int(input())
road = np.fromstring(input(), dtype=np.uint16, sep=' ', count=N)
result = 0


def solve(start: int, end: int):
    global result
    min_val: int = road[start:end].min()
    if min_val:
        result += min_val
        road[start:end] -= min_val
        solve(start, end)
    else:
        idxs = np.where(road[start:end] == 0)[0]
        i0 = 0
        for i in idxs:
            if i > i0:
                solve(start + i0, start + i)
            i0 = i + 1
        if start + i0 < end:
            solve(start + i0, end)


solve(0, N)
print(result)
