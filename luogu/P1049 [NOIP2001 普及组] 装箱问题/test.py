# P1049 [NOIP2001 普及组] 装箱问题 https://www.luogu.com.cn/problem/P1049

V = int(input())
N = int(input())
dp = [V] * (V + 1)
print(dp)

for _ in range(N):
    w = int(input())
    for j in range(V, w - 1, -1):
        dp[j] = min(dp[j], dp[j - w] - w)
    print(dp)
print(dp[V])
