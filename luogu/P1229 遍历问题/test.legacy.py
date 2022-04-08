# P1229 遍历问题 https://www.luogu.com.cn/problem/P1229

pre_order_seq = input().strip()
post_order_seq = input().strip()


def dfs(pre: str, post: str) -> int:
    pre_len = len(pre)
    if pre_len <= 1:
        return 1
    left_idx = post.index(pre[1])
    left_post, right_post = post[:left_idx + 1], post[left_idx + 1:-1]
    left_pre, right_pre = pre[1:left_idx + 2], pre[left_idx + 2:]
    left_cnt = dfs(left_pre, left_post)
    right_cnt = dfs(right_pre, right_post)
    return 2 * left_cnt * right_cnt if left_idx + 2 == pre_len else left_cnt * right_cnt


print(dfs(pre_order_seq, post_order_seq))
