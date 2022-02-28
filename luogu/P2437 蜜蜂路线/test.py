# P2437 蜜蜂路线 https://www.luogu.com.cn/problem/P2437

import sys

sys.setrecursionlimit(1010)
M, N = map(int, input().split())
mem = [0] * N


def dfs(i: int) -> int:
    if i >= N - 1:
        return 1
    if not mem[i]:
        mem[i] = dfs(i + 1) + dfs(i + 2)
    return mem[i]


print(dfs(M))
