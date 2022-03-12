# P2404 自然数的拆分问题
# https://www.luogu.com.cn/record/71252245

from typing import List

N = int(input())


def dfs(residue: int, nums: List[int]):
    if not residue:
        print('+'.join(map(str, nums)))
        return
    for i in range(nums[-1] if len(nums) else 1,
                   residue + 1 if len(nums) else residue):
        dfs(residue - i, nums + [i])


dfs(N, [])
