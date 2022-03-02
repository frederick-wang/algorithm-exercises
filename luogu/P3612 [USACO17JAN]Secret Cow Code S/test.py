# P3612 [USACO17JAN]Secret Cow Code S https://www.luogu.com.cn/problem/P3612

from math import ceil, log2

raw = input().split()
s = raw[0]
LEN = len(s)
N = int(raw[1])


def f(n: int) -> str:
    if n <= LEN:
        return s[n - 1]
    k = ceil(log2(n / LEN))
    lower_bound = 2**(k - 1) * LEN
    n -= lower_bound
    return f(lower_bound if n == 1 else n - 1)


print(f(N))
