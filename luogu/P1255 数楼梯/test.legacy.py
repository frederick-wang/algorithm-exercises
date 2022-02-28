# P1255 数楼梯 https://www.luogu.com.cn/problem/P1255
# https://www.luogu.com.cn/record/70276643
import sys

sys.setrecursionlimit(5010)

N = int(input())
record = [0] * (N + 1)


def dfs(i: int) -> int:
    if i >= N:
        return 1
    if not record[i]:
        record[i] = dfs(i + 1) + dfs(i + 2)
    return record[i]


print(dfs(1))
