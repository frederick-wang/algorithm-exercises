# P4913 【深基16.例3】二叉树深度 https://www.luogu.com.cn/problem/P4913

from typing import List
import sys

sys.setrecursionlimit(1000010)


class Node:
    left: int
    right: int

    def __init__(self, left: int = 0, right: int = 0):
        self.left = left
        self.right = right


N = int(input())
t: List[Node] = [Node() for _ in range(N + 1)]
for i in range(1, N + 1):
    l, r = map(int, input().split())
    t[i].left = l
    t[i].right = r


def dfs(x: int) -> int:
    return max(dfs(t[x].left), dfs(t[x].right)) + 1 if x else 0


print(dfs(1))
