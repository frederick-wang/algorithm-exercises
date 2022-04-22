# P1507 NASA的食物计划 https://www.luogu.com.cn/problem/P1507

import itertools
from array import array

MAX_V, MAX_M = map(int, input().split())
N = int(input())
v = array('I', [0]) * N
m = array('I', [0]) * N
c = array('I', [0]) * N
for i in range(N):
    v[i], m[i], c[i] = map(int, input().split())
dp = [[array('I', [0]) * (MAX_M + 1)
       for _ in range(MAX_V + 1)]
      for _ in range(N + 1)]
for i, j, k in itertools.product(range(N), range(MAX_V + 1), range(MAX_M + 1)):
    dp[i + 1][j][k] = dp[i][j][k] if j < v[i] or k < m[i] else max(
        dp[i][j][k], dp[i][j - v[i]][k - m[i]] + c[i])

print(dp[N][MAX_V][MAX_M])
