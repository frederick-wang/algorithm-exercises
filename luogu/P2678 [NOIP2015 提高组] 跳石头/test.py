# P2678 [NOIP2015 提高组] 跳石头 https://www.luogu.com.cn/problem/P2678

INF = int(1e9) + 1
L, N, M = map(int, input().split())
D = [0] + [int(input()) for _ in range(N)] + [L]


def estimate(min_span: int) -> int:
    num = 0
    tmp = D[:]
    for i in range(N + 1):
        span = tmp[i + 1] - tmp[i]
        if span < min_span:
            num += 1
            tmp[i + 1] -= span
    return num


lower_bound = 1
upper_bound = L
while lower_bound <= upper_bound:
    m = (lower_bound + upper_bound) >> 1
    estimated = estimate(m)
    if estimated <= M:
        lower_bound = m + 1
    else:
        upper_bound = m - 1
print(upper_bound)
