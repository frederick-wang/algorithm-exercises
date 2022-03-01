# P1164 小A点菜 https://www.luogu.com.cn/problem/P1164
# https://www.luogu.com.cn/record/70383132

from typing import List

N, M = map(int, input().split())
price: List[int] = []
while len(price) < N:
    price += list(map(int, input().split()))
mem = [[-1] * (M + 1) for _ in range(N)]


def dfs(i: int, money: int) -> int:
    if money > M:
        return 0
    if money == M:
        return 1
    if i >= N:
        return 0
    if mem[i][money] == -1:
        mem[i][money] = dfs(i + 1, money) + dfs(i + 1, money + price[i])
    return mem[i][money]


print(dfs(0, 0))
