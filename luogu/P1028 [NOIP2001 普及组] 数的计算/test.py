# P1028 [NOIP2001 普及组] 数的计算 https://www.luogu.com.cn/problem/P1028

N = int(input().strip())
table = [0] * (N + 1)
table[0] = 1

for i in range(1, N + 1):
    if i % 2:
        table[i] = table[i - 1]
    else:
        table[i] = table[i // 2] + table[i - 1]

print(table[N])
