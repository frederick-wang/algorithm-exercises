# P2392 kkksc03考前临时抱佛脚 https://www.luogu.com.cn/problem/P2392


def dfs(idx: int, one_side_sum: int):
    '''找到最接近 L_HALF_SUM 的数'''

    global min_time

    # 剪枝
    if one_side_sum >= min_time:
        return

    if one_side_sum >= L_HALF_SUM:
        # one_side_sum 一定大于等于 L_HALF_SUM - one_side_sum
        min_time = min(min_time, one_side_sum)
        return

    for j in range(idx, len(L)):
        dfs(j + 1, one_side_sum + L[j])


s1, s2, s3, s4 = map(int, input().split())

result = 0
for _ in range(4):
    min_time = 1000000
    L = tuple(map(int, input().split()))
    L_SUM = sum(L)
    L_HALF_SUM = L_SUM // 2 + L_SUM % 2
    dfs(0, 0)
    result += min_time

print(result)
