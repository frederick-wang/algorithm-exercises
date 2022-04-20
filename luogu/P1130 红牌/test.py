# P1130 红牌 https://www.luogu.com.cn/problem/P1130
# 需要用 PyPy3 提交

from itertools import product

N, M = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(M)]
dp = [[0] * N for _ in range(M)]
ans = int(1e10)
for j, i in product(range(N - 1, -1, -1), range(M)):
    if j == N - 1:
        dp[i][j] = a[i][j]
        continue
    dp[i][j] = min(dp[i][j + 1], dp[(i + 1) % M][j + 1]) + a[i][j]
print(min(map(lambda x: x[0], dp)))
