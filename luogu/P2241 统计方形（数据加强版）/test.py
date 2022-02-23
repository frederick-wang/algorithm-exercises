# P2241 统计方形（数据加强版） https://www.luogu.com.cn/problem/P2241

N, M = map(int, input().split())

total = M * (M + 1) * N * (N + 1) // 4
square_count = 0

for i in range(min(M, N)):
    square_count += (M - i) * (N - i)

print(square_count, total - square_count)
