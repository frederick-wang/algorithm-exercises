# P2089 烤鸡 https://www.luogu.com.cn/problem/P2089

from typing import List

N = int(input())

if N < 10 or N > 30:
    print(0)
    exit()

out_strs: List[str] = []


def dfs(idx: int, cur_sum: int, seasonings: str):
    if cur_sum > N:
        return
    if idx == 10:
        if cur_sum == N:
            out_strs.append(seasonings)
        return
    for i in (1, 2, 3):
        dfs(idx + 1, cur_sum + i, seasonings + f'{i} ')


dfs(0, 0, '')
print(len(out_strs))
print('\n'.join(out_strs))
