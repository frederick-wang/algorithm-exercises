# P1088 [NOIP2004 普及组] 火星人 https://www.luogu.com.cn/problem/P1088

import sys

sys.setrecursionlimit(10010)

N = int(input())
m = int(input())
nums = list(map(int, input().split()))

result = [0] * N
unused = [1] * (1 + N)
remembered = [0] * N

templ = ' '.join('%d' for _ in range(N))


def dfs(i: int):
    global m

    if i == N:
        m -= 1
        return

    for j in range(1 if remembered[i] else nums[i], N + 1):
        if unused[j]:
            result[i] = j
            unused[j] = 0
            dfs(i + 1)
            if m < 0:
                return
            unused[j] = 1
    if not remembered[i]:
        remembered[i] = 1


dfs(0)

print(templ % tuple(result))
