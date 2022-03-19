# P1102 A-B 数对 https://www.luogu.com.cn/problem/P1102

from collections import Counter

N, C = map(int, input().split())
d = Counter(map(int, input().split()))
cnt = 0
for a in d:
    b = a - C
    if b in d:
        cnt += d[a] * d[b]
print(cnt)
