# P1060 [NOIP2006 普及组] 开心的金明 https://www.luogu.com.cn/problem/P1060

from array import array

N, M = map(int, input().split())
f = array('I', [0]) * (N + 1)
for _ in range(M):
    v, p = map(int, input().split())
    for j in range(N, v - 1, -1):
        f[j] = max(f[j], f[j - v] + p * v)
print(f[N])
