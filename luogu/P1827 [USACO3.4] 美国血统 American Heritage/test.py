# P1827 [USACO3.4] 美国血统 American Heritage https://www.luogu.com.cn/problem/P1827

from typing import List, Optional


class Node:
    val: str
    left: Optional['Node']
    right: Optional['Node']

    def __init__(self,
                 val: str,
                 left: Optional['Node'] = None,
                 right: Optional['Node'] = None):
        self.val = val
        self.left = left
        self.right = right


in_order_list = list(input().strip())
pre_order_list = list(input().strip())


def parse(in_order: List[str], pre_order: List[str]) -> Optional[Node]:
    if not in_order:
        return None
    node = Node(pre_order.pop(0))
    idx = in_order.index(node.val)
    left = in_order[:idx]
    right = in_order[idx + 1:]
    node.left = parse(left, pre_order[:len(left)])
    node.right = parse(right, pre_order[len(left):])
    return node


def post_order_traverse(node: Optional[Node]) -> str:
    return post_order_traverse(node.left) + post_order_traverse(
        node.right) + node.val if node else ''


print(post_order_traverse(parse(in_order_list, pre_order_list)))
