# P3853 [TJOI2007]路标设置 https://www.luogu.com.cn/problem/P3853
# https://www.luogu.com.cn/record/72133175

L, N, K = map(int, input().split())
signs = list(map(int, input().split()))
d = [0] * (N - 1)
for i in range(N - 1):
    d[i] = signs[i + 1] - signs[i]


def simulate(max_span: int) -> bool:
    addition = 0
    for span in d:
        if span > max_span:
            addition += (span - 1) // max_span
            if addition > K:
                return False
    return addition <= K


lower_bound = 1
upper_bound = max(d)

while lower_bound <= upper_bound:
    m = (lower_bound + upper_bound) >> 1
    if simulate(m):
        upper_bound = m - 1
    else:
        lower_bound = m + 1
print(lower_bound)
