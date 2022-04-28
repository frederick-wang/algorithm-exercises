# P1060 [NOIP2006 普及组] 开心的金明 https://www.luogu.com.cn/problem/P1060

N, M = map(int, input().split())
f = [[0] * (N + 1) for _ in range(M + 1)]
for i in range(M):
    v, p = map(int, input().split())
    for j in range(N + 1):
        f[i + 1][j] = f[i][j] if j < v else max(f[i][j], f[i][j - v] + p * v)
print(f[M][N])
