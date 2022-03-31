# P1305 新二叉树 https://www.luogu.com.cn/problem/P1305

from typing import List, Optional


class Node:
    val: str
    left: Optional['Node']
    right: Optional['Node']

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


nodes: List[Optional[Node]] = [None] * 26
first_root = Node('')
N = int(input())
for i in range(N):
    root, left, right = tuple(input().strip())
    if tmp := nodes[ord(root) - 97]:
        node_root = tmp
    else:
        node_root = Node(root)
        nodes[ord(root) - 97] = node_root
    if not i:
        first_root = node_root
    if left != '*':
        node_left = Node(left)
        nodes[ord(left) - 97] = node_left
        node_root.left = node_left
    if right != '*':
        node_right = Node(right)
        nodes[ord(right) - 97] = node_right
        node_root.right = node_right


def to_str(node: Node) -> str:
    result = node.val
    if node.left:
        result += to_str(node.left)
    if node.right:
        result += to_str(node.right)
    return result


print(to_str(first_root))
