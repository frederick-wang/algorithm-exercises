# P3884 [JLOI2009]二叉树问题 https://www.luogu.com.cn/problem/P3884

from typing import Optional


class Node:
    val: int
    depth: int
    parent: Optional['Node']
    left: Optional['Node']
    right: Optional['Node']

    def __init__(self, val: int, depth=1):
        self.val = val
        self.depth = depth
        self.left = None
        self.right = None


N = int(input())
nodes = [Node(i) for i in range(N + 1)]  # 所有节点
width = [0] * (N + 1)  # 不同深度的宽度
width[1] = 1 # 初始化深度 1 的宽度为 1（根节点只有 1 个）
for _ in range(N - 1):
    x, y = map(int, input().split())
    nodes[y].parent = nodes[x]
    nodes[y].depth = nodes[x].depth + 1
    width[nodes[y].depth] += 1
    if not nodes[x].left:
        nodes[x].left = nodes[y]
    else:
        nodes[x].right = nodes[y]
print(max(map(lambda x: x.depth, nodes)))
print(max(width))
u, v = map(int, input().split())
distance = 0
while nodes[u].depth > nodes[v].depth:
    if parent := nodes[u].parent:
        u = parent.val
        distance += 2
while nodes[v].depth > nodes[u].depth:
    if parent := nodes[v].parent:
        v = parent.val
        distance += 1
while u != v:
    if parent := nodes[u].parent:
        u = parent.val
        distance += 2
    if parent := nodes[v].parent:
        v = parent.val
        distance += 1
print(distance)
