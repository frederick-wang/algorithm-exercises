# P1855 榨取kkksc03 https://www.luogu.com.cn/problem/P1855

from itertools import product

N, M, T = map(int, input().split())
dp = [[[0] * (T + 1) for _ in range(M + 1)] for _ in range(N + 1)]
for i in range(N):
    m, t = map(int, input().split())
    for j, k in product(range(M + 1), range(T + 1)):
        if j < m or k < t:
            dp[i + 1][j][k] = dp[i][j][k]
        else:
            dp[i + 1][j][k] = max(dp[i][j][k], dp[i][j - m][k - t] + 1)
print(dp[N][M][T])
