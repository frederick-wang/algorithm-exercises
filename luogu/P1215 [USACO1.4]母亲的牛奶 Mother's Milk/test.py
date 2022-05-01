# P1215 [USACO1.4]母亲的牛奶 Mother's Milk https://www.luogu.com.cn/problem/P1215

from typing import List

A, B, C = map(int, input().split())
vis = [[[False] * (C + 1) for _ in range(B + 1)] for _ in range(A + 1)]
result: List[int] = []


def dfs(a: int, b: int, c: int):
    if vis[a][b][c]:
        return
    vis[a][b][c] = True
    if not a:
        result.append(c)
    a_space = A - a
    b_space = B - b
    c_space = C - c
    # a 倒入 b
    diff = min(a, b_space)
    dfs(a - diff, b + diff, c)
    # a 倒入 c
    diff = min(a, c_space)
    dfs(a - diff, b, c + diff)
    # b 倒入 a
    diff = min(b, a_space)
    dfs(a + diff, b - diff, c)
    # b 倒入 c
    diff = min(b, c_space)
    dfs(a, b - diff, c + diff)
    # c 倒入 a
    diff = min(c, a_space)
    dfs(a + diff, b, c - diff)
    # c 倒入 b
    diff = min(c, b_space)
    dfs(a, b + diff, c - diff)


dfs(0, 0, C)
result.sort()
print(*result)
