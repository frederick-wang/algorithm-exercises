# P2615 [NOIP2015 提高组] 神奇的幻方 https://www.luogu.com.cn/problem/P2615

N = int(input())
s = [[0] * N for _ in range(N)]
x = N // 2
y = 0
s[y][x] = 1
for K in range(2, N**2 + 1):
    if x == N - 1 and y == 0:
        x_k = x
        y_k = y + 1
    else:
        x_k = x + 1 if x < N - 1 else 0
        y_k = y - 1 if y > 0 else N - 1
    if s[y_k][x_k]:
        x_k = x
        y_k = y + 1
    s[y_k][x_k] = K
    x = x_k
    y = y_k

print('\n'.join(map(lambda row: ' '.join(map(str, row)), s)))
