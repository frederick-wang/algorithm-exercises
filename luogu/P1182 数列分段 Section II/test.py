# P1182 数列分段 Section II https://www.luogu.com.cn/problem/P1182

N, M = map(int, input().split())
A = list(map(int, input().split()))


def simulate(max_val: int) -> bool:
    seg_num = 1
    s = 0
    for a in A:
        if a > max_val:
            return False
        s += a
        if s > max_val:
            seg_num += 1
            s = a
    return seg_num <= M


lower_bound = max(A)
upper_bound = sum(A)
while lower_bound <= upper_bound:
    m = (lower_bound + upper_bound) // 2
    sm = simulate(m)
    if sm:
        upper_bound = m - 1
    else:
        lower_bound = m + 1
print(lower_bound)
