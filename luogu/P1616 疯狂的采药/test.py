# P1616 疯狂的采药 https://www.luogu.com.cn/problem/P1616

from array import array

T, M = map(int, input().split())
dp = array('L', [0]) * (T + 1)

for _ in range(M):
    t, v = map(int, input().split())
    for j in range(t, T + 1):
        dp[j] = max(dp[j], dp[j - t] + v)
print(dp[T])
