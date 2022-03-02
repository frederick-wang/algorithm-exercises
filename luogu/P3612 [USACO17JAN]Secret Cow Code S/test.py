# P3612 [USACO17JAN]Secret Cow Code S https://www.luogu.com.cn/problem/P3612
# https://www.luogu.com.cn/record/70445357

from math import ceil, log2

raw = input().split()
s = raw[0]
LEN = len(s)
n = int(raw[1])

while n > LEN:
    k = ceil(log2(n / LEN))
    lower_bound = 2**(k - 1) * LEN
    n -= lower_bound
    if n == 1:
        n = lower_bound
    else:
        n -= 1

print(s[n - 1])
