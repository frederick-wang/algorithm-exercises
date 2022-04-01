# P1030 [NOIP2001 普及组] 求先序排列 https://www.luogu.com.cn/problem/P1030

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
post_order_list = list(input().strip())


def parse(
    in_order: List[str],
    post_order: List[str],
) -> Optional[Node]:
    if not in_order or not post_order:
        return None
    root = Node(post_order.pop())
    root_idx = in_order.index(root.val)
    left_list = in_order[:root_idx]
    right_list = in_order[root_idx + 1:]
    root.left = parse(left_list, post_order[:len(left_list)])
    root.right = parse(right_list, post_order[len(left_list):])
    return root


def pre_order_traversal(node: Optional[Node]) -> str:
    return (node.val + pre_order_traversal(node.left) +
            pre_order_traversal(node.right)) if node else ''


print(pre_order_traversal(parse(in_order_list, post_order_list)))
