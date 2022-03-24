# P1160 队列安排 https://www.luogu.com.cn/problem/P1160

from __future__ import annotations
from typing import List, Optional


class Node:
    val: int
    prev: Optional[Node]
    next: Optional[Node]

    def __init__(self, val: int, prev: Optional[Node],
                 next: Optional[Node]) -> None:
        self.val = val
        self.prev = prev
        self.next = next


N = int(input())
node: List[Optional[Node]] = [None] * (N + 1)
head = Node(0, None, None)
head.next = Node(1, head, None)
node[1] = head.next
for i in range(2, N + 1):
    k, p = map(int, input().split())
    if k_node := node[k]:
        i_node = Node(i, None, None)
        node[i] = i_node
        if p:
            r_node = k_node.next
            i_node.prev = k_node
            i_node.next = r_node
            if r_node:
                r_node.prev = i_node
            k_node.next = i_node
        else:
            l_node = k_node.prev
            i_node.prev = l_node
            i_node.next = k_node
            if l_node:
                l_node.next = i_node
            k_node.prev = i_node
M = int(input())
for _ in range(M):
    x = int(input())
    if x_node := node[x]:
        l_node = x_node.prev
        r_node = x_node.next
        if l_node:
            l_node.next = r_node
        if r_node:
            r_node.prev = l_node
        node[x] = None
point: Optional[Node] = head.next
while point:
    print(point.val, end=' ' if point.next else '\n')
    point = point.next
